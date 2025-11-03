# ?? One-Click Canva?Next.js Builder

## Overview

This feature adds a powerful one-click pipeline to convert Canva websites into fully functional Next.js projects with automatic GitHub deployment and email notifications.

## Features

? **Complete Automation Pipeline:**
1. ?? **Crawl Canva Site** - Downloads entire website including assets
2. ?? **Convert to Next.js** - Creates modern Next.js + Tailwind CSS project
3. ?? **RTL Support** - Automatic right-to-left (Arabic) text direction
4. ?? **ZIP Package** - Compresses project for distribution
5. ?? **GitHub Release** - Uploads to GitHub with automatic versioning
6. ?? **Email Notification** - Sends download link via SendGrid

## Usage

### Command Palette

1. Press `Cmd/Ctrl + Shift + P`
2. Type: `Canva?Next.js: One-Click Builder`
3. Follow the prompts to enter:
   - Canva site URL
   - GitHub repository (username/repo)
   - GitHub Personal Access Token
   - Notification email
   - SendGrid API Key (optional)

### Configuration

Set default values in VS Code settings:

```json
{
  "promptPerfect.canvaBuilder.defaultTargetUrl": "https://muqtasr.my.canva.site/",
  "promptPerfect.canvaBuilder.defaultGithubRepo": "username/repo",
  "promptPerfect.canvaBuilder.defaultEmail": "your@email.com"
}
```

## Requirements

### System Dependencies

- **wget** - For website crawling
- **zip** - For package compression
- **Node.js** - For Next.js project creation

Install on Ubuntu/Debian:
```bash
sudo apt-get install wget zip
```

Install on macOS:
```bash
brew install wget
```

### GitHub Personal Access Token

Create a token at: https://github.com/settings/tokens

Required scopes:
- `repo` - Full control of private repositories
- `workflow` - Update GitHub Action workflows
- `write:packages` - Upload packages

### SendGrid API Key (Optional)

For email notifications:
1. Create account at: https://sendgrid.com
2. Generate API key at: https://app.sendgrid.com/settings/api_keys
3. Verify sender email

## Output Structure

The pipeline creates the following in your workspace:

```
workspace/
??? rebuild/
?   ??? html/           # Downloaded Canva site
?   ??? data.json       # Extracted page data
??? site-clone/         # Generated Next.js project
?   ??? src/
?   ?   ??? app/
?   ?       ??? page.tsx       # Home page
?   ?       ??? [pages]/       # Additional pages
?   ??? package.json
?   ??? ...
??? site-clone.zip      # Distribution package
??? download_link.txt   # GitHub release URL
```

## Generated Next.js Project

### Features
- ? TypeScript
- ? Tailwind CSS
- ? RTL Support
- ? App Router
- ? ESLint
- ? Modern UI

### Arabic Font Support
The generated CSS includes:
```css
body {
  direction: rtl;
  font-family: "Tajawal", "Cairo", sans-serif;
}
```

## Progress Monitoring

During execution, check:
1. **Output Panel** - Select "Canva Builder" from dropdown
2. **Progress Notification** - Bottom-right corner
3. **Status Messages** - Top of window

## Troubleshooting

### wget Command Not Found
```bash
# Ubuntu/Debian
sudo apt-get install wget

# macOS
brew install wget
```

### zip Command Not Found
```bash
# Ubuntu/Debian
sudo apt-get install zip

# macOS
# Already included in macOS
```

### GitHub API Errors

**401 Unauthorized:**
- Check your Personal Access Token
- Verify token has required scopes

**404 Not Found:**
- Verify repository name format: `username/repo`
- Ensure repository exists
- Check token has access to repository

### Email Not Sending

**SendGrid API Key Issues:**
- Verify API key is valid
- Check sender email is verified in SendGrid
- Review SendGrid dashboard for errors

**Skipping Email:**
- Email notification is optional
- Pipeline continues if email fails

## Example Workflow

```
Input: https://muqtasr.my.canva.site/my-site
       username/my-repo
       ghp_xxxxxxxxxxxx
       user@example.com
       SG.xxxxxxxxxxxxx

Output:
??? ? Site crawled (45 files)
??? ? Next.js project created
??? ? 3 pages generated
??? ? Tailwind configured
??? ? ZIP created (2.5 MB)
??? ? GitHub release uploaded
?   ??? https://github.com/username/my-repo/releases/tag/auto-2025-11-03
??? ? Email sent to user@example.com
```

## Advanced Usage

### Manual Deployment

After the pipeline completes:

```bash
cd site-clone
npm install
npm run dev    # Development server
npm run build  # Production build
```

### Custom Domain

To use a custom domain with GitHub Pages:
1. Add `CNAME` file to `site-clone/public/`
2. Configure DNS settings
3. Enable custom domain in repository settings

## API Reference

### `CanvaToNextJsBuilder` Class

```typescript
class CanvaToNextJsBuilder {
  constructor(workspaceRoot: string)
  
  async runPipeline(inputs: PipelineInputs): Promise<string>
  
  // Returns: Download link to GitHub release
}
```

### `PipelineInputs` Interface

```typescript
interface PipelineInputs {
  targetUrl: string;        // Canva site URL
  githubRepo: string;       // Format: username/repo
  githubToken: string;      // GitHub PAT
  notifyEmail: string;      // Notification recipient
  sendgridApiKey: string;   // SendGrid API key (optional)
}
```

## Security Notes

?? **Important Security Considerations:**

1. **Never commit tokens:**
   - GitHub tokens are entered securely (password field)
   - Not saved in configuration
   - Not written to disk

2. **Token permissions:**
   - Use tokens with minimum required scopes
   - Consider using fine-grained tokens
   - Rotate tokens regularly

3. **SendGrid API keys:**
   - Keep API keys confidential
   - Use environment variables in production
   - Monitor usage in SendGrid dashboard

## Support

For issues or questions:
- Check the Output Panel for detailed logs
- Review error messages in notifications
- Verify all dependencies are installed

## Author

????????? ??????? ??????? (Abdulaziz Ibrahim Al-Khalfan)

## License

Same as Prompt Perfect extension
