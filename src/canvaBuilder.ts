import * as vscode from 'vscode';
import * as fs from 'fs';
import * as path from 'path';
import * as child_process from 'child_process';
import { promisify } from 'util';
import fetch from 'node-fetch';

const exec = promisify(child_process.exec);

interface PipelineInputs {
	targetUrl: string;
	githubRepo: string;
	githubToken: string;
	notifyEmail: string;
	sendgridApiKey: string;
}

interface PageData {
	title: string;
	body: string;
}

export class CanvaToNextJsBuilder {
	private workspaceRoot: string;
	private outputChannel: vscode.OutputChannel;

	constructor(workspaceRoot: string) {
		this.workspaceRoot = workspaceRoot;
		this.outputChannel = vscode.window.createOutputChannel('Canva Builder');
	}

	private log(message: string) {
		this.outputChannel.appendLine(`[${new Date().toLocaleTimeString()}] ${message}`);
		console.log(message);
	}

	private async execCommand(command: string, cwd?: string): Promise<{ stdout: string; stderr: string }> {
		this.log(`Executing: ${command}`);
		try {
			const result = await exec(command, { cwd: cwd || this.workspaceRoot, maxBuffer: 10 * 1024 * 1024 });
			return result;
		} catch (error) {
			const errorMessage = error instanceof Error ? error.message : String(error);
			this.log(`Error: ${errorMessage}`);
			throw error;
		}
	}

	async runPipeline(inputs: PipelineInputs): Promise<string> {
		this.outputChannel.show();
		this.log('?? Starting One-Click Canva?Next.js Pipeline...');

		try {
			// Step 1: Crawl and rebuild
			await this.crawlAndRebuild(inputs.targetUrl);

			// Step 2: Extract and generate pages
			await this.extractAndGeneratePages();

			// Step 3: Setup Tailwind and assets
			await this.setupTailwindAndAssets();

			// Step 4: Zip package
			const zipPath = await this.zipPackage();

			// Step 5: Upload to GitHub Release
			const downloadLink = await this.uploadReleaseAndEnablePages(
				inputs.githubRepo,
				inputs.githubToken,
				zipPath
			);

			// Step 6: Send email notification
			await this.sendEmailNotification(
				inputs.notifyEmail,
				inputs.sendgridApiKey,
				downloadLink
			);

			this.log('? Pipeline completed successfully!');
			vscode.window.showInformationMessage(
				`? Build complete! Download: ${downloadLink}`
			);

			return downloadLink;
		} catch (error) {
			const errorMessage = error instanceof Error ? error.message : String(error);
			this.log(`? Pipeline failed: ${errorMessage}`);
			vscode.window.showErrorMessage(`Pipeline failed: ${errorMessage}`);
			throw error;
		}
	}

	private async crawlAndRebuild(targetUrl: string): Promise<void> {
		this.log('?? Step 1: Crawling Canva site...');

		const rebuildDir = path.join(this.workspaceRoot, 'rebuild');
		const htmlDir = path.join(rebuildDir, 'html');

		// Create directories
		if (!fs.existsSync(htmlDir)) {
			fs.mkdirSync(htmlDir, { recursive: true });
		}

		// Extract domain from URL
		const urlObj = new URL(targetUrl);
		const domain = urlObj.hostname;

		// Crawl the website
		const wgetCmd = `wget --recursive --no-clobber --page-requisites --adjust-extension --convert-links --span-hosts --domains ${domain},cdn.canva.com --no-parent "${targetUrl}" -P "${htmlDir}"`;
		
		await this.execCommand(wgetCmd);

		// Create Next.js app
		this.log('?? Creating Next.js application...');
		const nextAppPath = path.join(this.workspaceRoot, 'site-clone');
		
		if (fs.existsSync(nextAppPath)) {
			this.log('Removing existing site-clone directory...');
			fs.rmSync(nextAppPath, { recursive: true, force: true });
		}

		await this.execCommand(
			`npx create-next-app@latest site-clone --typescript --tailwind --eslint --app --src-dir --no-install --no-git`
		);

		this.log('? Crawl and rebuild completed');
	}

	private async extractAndGeneratePages(): Promise<void> {
		this.log('?? Step 2: Extracting and generating pages...');

		const rebuildDir = path.join(this.workspaceRoot, 'rebuild');
		const htmlDir = path.join(rebuildDir, 'html');
		const siteCloneDir = path.join(this.workspaceRoot, 'site-clone');

		// Find all HTML files
		const htmlFiles = this.findHtmlFiles(htmlDir);
		this.log(`Found ${htmlFiles.length} HTML files`);

		const pages: PageData[] = [];
		const assets = new Set<string>();

		// Extract content from each HTML file
		for (const htmlFile of htmlFiles) {
			const content = fs.readFileSync(htmlFile, 'utf8');
			
			// Extract title
			const titleMatch = content.match(/<title>(.*?)<\/title>/i);
			const title = titleMatch ? titleMatch[1] : path.basename(htmlFile, '.html');

			// Extract body
			const bodyMatch = content.match(/<body[^>]*>([\s\S]*)<\/body>/i);
			const body = bodyMatch ? bodyMatch[1] : '';

			// Extract images
			const imgMatches = content.matchAll(/<img[^>]+src=["']([^"']+)["']/gi);
			for (const match of imgMatches) {
				assets.add(match[1]);
			}

			pages.push({ title, body });
		}

		// Save extracted data
		const dataJson = { pgs: pages, assets: Array.from(assets) };
		fs.writeFileSync(
			path.join(rebuildDir, 'data.json'),
			JSON.stringify(dataJson, null, 2)
		);

		// Generate Next.js pages
		const appDir = path.join(siteCloneDir, 'src', 'app');
		
		pages.forEach((page, index) => {
			const pageName = index === 0 
				? 'page' 
				: this.sanitizePageName(page.title);
			
			const componentName = pageName.charAt(0).toUpperCase() + pageName.slice(1).replace(/-/g, '');
			const pageContent = `import React from 'react';

export default function ${componentName}() {
  return (
    <main className="prose max-w-4xl mx-auto p-6">
      <h1>${this.escapeHtml(page.title)}</h1>
      <div dangerouslySetInnerHTML={{ __html: \`${this.escapeBackticks(page.body)}\` }} />
    </main>
  );
}
`;

			const fileName = index === 0 ? 'page.tsx' : `${pageName}/page.tsx`;
			const filePath = path.join(appDir, fileName);
			
			// Create directory if needed
			const dir = path.dirname(filePath);
			if (!fs.existsSync(dir)) {
				fs.mkdirSync(dir, { recursive: true });
			}
			
			fs.writeFileSync(filePath, pageContent);
			this.log(`Created page: ${fileName}`);
		});

		this.log('? Page extraction completed');
	}

	private async setupTailwindAndAssets(): Promise<void> {
		this.log('?? Step 3: Setting up Tailwind and assets...');

		const siteCloneDir = path.join(this.workspaceRoot, 'site-clone');
		const globalsPath = path.join(siteCloneDir, 'src', 'app', 'globals.css');

		const tailwindConfig = `@tailwind base;
@tailwind components;
@tailwind utilities;

body {
  direction: rtl;
  font-family: "Tajawal", "Cairo", sans-serif;
}

.prose {
  max-width: 100%;
}
`;

		fs.writeFileSync(globalsPath, tailwindConfig);
		this.log('? Tailwind setup completed');
	}

	private async zipPackage(): Promise<string> {
		this.log('?? Step 4: Creating ZIP package...');

		const siteCloneDir = path.join(this.workspaceRoot, 'site-clone');
		const zipPath = path.join(this.workspaceRoot, 'site-clone.zip');

		// Remove old zip if exists
		if (fs.existsSync(zipPath)) {
			fs.unlinkSync(zipPath);
		}

		await this.execCommand(`zip -r "../site-clone.zip" .`, siteCloneDir);

		this.log(`? ZIP created: ${zipPath}`);
		return zipPath;
	}

	private async uploadReleaseAndEnablePages(
		repo: string,
		token: string,
		zipPath: string
	): Promise<string> {
		this.log('?? Step 5: Uploading to GitHub Release...');

		const zipBuffer = fs.readFileSync(zipPath);
		const tag = `auto-${new Date().toISOString().split('T')[0]}-${Date.now()}`;

		// Create release
		this.log(`Creating release with tag: ${tag}`);
		const createReleaseResponse = await fetch(
			`https://api.github.com/repos/${repo}/releases`,
			{
				method: 'POST',
				headers: {
					Authorization: `token ${token}`,
					'Content-Type': 'application/json',
					'User-Agent': 'VSCode-Extension'
				},
				body: JSON.stringify({
					tag_name: tag,
					name: `Auto Build - ${new Date().toLocaleString('ar')}`,
					body: '?? ?? ????? ??? ?????? ???????? ?? Canva ??? Next.js',
					draft: false,
					prerelease: false
				})
			}
		);

		if (!createReleaseResponse.ok) {
			const error = await createReleaseResponse.text();
			throw new Error(`Failed to create release: ${error}`);
		}

		const release = await createReleaseResponse.json();
		this.log(`Release created: ${release.html_url}`);

		// Upload asset
		const uploadUrl = release.upload_url.split('{')[0] + '?name=site-clone.zip';
		this.log('Uploading ZIP asset...');

		const uploadResponse = await fetch(uploadUrl, {
			method: 'POST',
			headers: {
				Authorization: `token ${token}`,
				'Content-Type': 'application/zip',
				'User-Agent': 'VSCode-Extension'
			},
			body: zipBuffer
		});

		if (!uploadResponse.ok) {
			const error = await uploadResponse.text();
			throw new Error(`Failed to upload asset: ${error}`);
		}

		const asset = await uploadResponse.json();
		const downloadLink = asset.browser_download_url;

		// Save download link
		fs.writeFileSync(
			path.join(this.workspaceRoot, 'download_link.txt'),
			downloadLink
		);

		this.log(`? Upload completed: ${downloadLink}`);
		return downloadLink;
	}

	private async sendEmailNotification(
		to: string,
		apiKey: string,
		downloadLink: string
	): Promise<void> {
		this.log('?? Step 6: Sending email notification...');

		if (!apiKey || apiKey === 'YOUR_SENDGRID_API_KEY') {
			this.log('?? SendGrid API key not configured, skipping email');
			return;
		}

		const response = await fetch('https://api.sendgrid.com/v3/mail/send', {
			method: 'POST',
			headers: {
				Authorization: `Bearer ${apiKey}`,
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				personalizations: [{ to: [{ email: to }] }],
				from: { email: 'no-reply@canva-builder.system' },
				subject: '? ?? ????? ???? ?????? ?????',
				content: [
					{
						type: 'text/html',
						value: `
<div dir="rtl" style="font-family: 'Tajawal', Arial, sans-serif; padding: 20px;">
  <h2 style="color: #00c851;">? ?? ????? ?????? ?????</h2>
  <p style="font-size: 16px;">?? ????? ???? Canva ??? ????? Next.js ?????!</p>
  <div style="margin: 20px 0; padding: 15px; background: #f5f5f5; border-radius: 8px;">
    <p style="margin: 0;"><strong>?? ???? ????? ZIP:</strong></p>
    <a href="${downloadLink}" style="color: #007bff; text-decoration: none; font-size: 14px;">${downloadLink}</a>
  </div>
  <p style="color: #666; font-size: 14px;">????? ???? ????? ??????? ????? ??? ?? ???????.</p>
</div>
`
					}
				]
			})
		});

		if (!response.ok) {
			const error = await response.text();
			this.log(`?? Email sending failed: ${error}`);
		} else {
			this.log('? Email notification sent');
		}
	}

	// Helper methods
	private findHtmlFiles(dir: string, files: string[] = []): string[] {
		const entries = fs.readdirSync(dir, { withFileTypes: true });

		for (const entry of entries) {
			const fullPath = path.join(dir, entry.name);
			if (entry.isDirectory()) {
				this.findHtmlFiles(fullPath, files);
			} else if (entry.name.endsWith('.html')) {
				files.push(fullPath);
			}
		}

		return files;
	}

	private sanitizePageName(title: string): string {
		return title
			.toLowerCase()
			.replace(/[^\w\s-]/g, '')
			.replace(/\s+/g, '-')
			.replace(/-+/g, '-')
			.trim();
	}

	private escapeHtml(text: string): string {
		return text
			.replace(/&/g, '&amp;')
			.replace(/</g, '&lt;')
			.replace(/>/g, '&gt;')
			.replace(/"/g, '&quot;')
			.replace(/'/g, '&#039;');
	}

	private escapeBackticks(text: string): string {
		return text.replace(/`/g, '\\`').replace(/\$/g, '\\$');
	}
}

export async function promptForInputs(): Promise<PipelineInputs | undefined> {
	const config = vscode.workspace.getConfiguration('promptPerfect.canvaBuilder');

	// Get target URL
	const targetUrl = await vscode.window.showInputBox({
		prompt: 'Enter Canva site URL',
		value: config.get('defaultTargetUrl') || 'https://muqtasr.my.canva.site/',
		placeHolder: 'https://muqtasr.my.canva.site/your-site'
	});

	if (!targetUrl) return undefined;

	// Get GitHub repo
	const githubRepo = await vscode.window.showInputBox({
		prompt: 'Enter GitHub repository (username/repo)',
		value: config.get('defaultGithubRepo') || '',
		placeHolder: 'username/repository'
	});

	if (!githubRepo) return undefined;

	// Get GitHub token
	const githubToken = await vscode.window.showInputBox({
		prompt: 'Enter GitHub Personal Access Token (PAT)',
		password: true,
		placeHolder: 'ghp_xxxxxxxxxxxx'
	});

	if (!githubToken) return undefined;

	// Get notification email
	const notifyEmail = await vscode.window.showInputBox({
		prompt: 'Enter notification email',
		value: config.get('defaultEmail') || '',
		placeHolder: 'your.email@domain.com'
	});

	if (!notifyEmail) return undefined;

	// Get SendGrid API key (optional)
	const sendgridApiKey = await vscode.window.showInputBox({
		prompt: 'Enter SendGrid API Key (optional, skip to not send email)',
		password: true,
		placeHolder: 'SG.xxxxxxxxxxxx'
	});

	return {
		targetUrl,
		githubRepo,
		githubToken,
		notifyEmail,
		sendgridApiKey: sendgridApiKey || ''
	};
}

export async function runCanvaBuilderCommand() {
	const workspaceRoot = vscode.workspace.workspaceFolders?.[0].uri.fsPath;

	if (!workspaceRoot) {
		vscode.window.showErrorMessage('No workspace folder is open');
		return;
	}

	// Prompt for inputs
	const inputs = await promptForInputs();
	if (!inputs) {
		vscode.window.showInformationMessage('Build cancelled');
		return;
	}

	// Confirm before starting
	const confirm = await vscode.window.showWarningMessage(
		'This will create a new Next.js project in your workspace. Continue?',
		'Yes',
		'No'
	);

	if (confirm !== 'Yes') {
		return;
	}

	// Run the pipeline
	const builder = new CanvaToNextJsBuilder(workspaceRoot);
	
	await vscode.window.withProgress(
		{
			location: vscode.ProgressLocation.Notification,
			title: 'Building Canva?Next.js',
			cancellable: false
		},
		async (progress) => {
			progress.report({ message: 'Starting pipeline...' });
			await builder.runPipeline(inputs);
		}
	);
}
