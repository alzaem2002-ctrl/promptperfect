# ?? Canva?Next.js One-Click Builder & Publisher

Automated agent that converts Canva sites to Next.js projects and publishes them to GitHub.

## ?? Features

- ? Automatically download Canva site
- ? Create Next.js + Tailwind CSS project with RTL support
- ? Convert HTML pages to React components
- ? Compress project to ZIP
- ? Upload to GitHub Releases
- ? Automatically enable GitHub Pages
- ? Send email notifications (optional)

## ?? Prerequisites

1. **wget** - To download Canva site
2. **zip** - To compress the project
3. **Node.js** - To run conversion scripts
4. **npx** - To create Next.js project
5. **GitHub Token** - To access GitHub API
6. **SendGrid API Key** (optional) - For email notifications

## ?? Setup

### 1. Getting GitHub Token

1. Go to [GitHub Settings > Developer settings > Personal access tokens > Tokens (classic)](https://github.com/settings/tokens)
2. Click **"Generate new token (classic)"**
3. Give the token a name (e.g., "Canva to Next.js Builder")
4. Select the following permissions:
   - ? `repo` - Full control of private repositories
   - ? `workflow` - Update GitHub Action workflows
   - ? `write:packages` (optional - if you want to upload packages)
5. Click **"Generate token"**
6. **Copy the token immediately** (you won't be able to see it again!)

**Important**: Store the token securely and never share it.

### 2. Getting SendGrid API Key (Optional)

If you want email notifications when the process completes:

1. Sign up for a [SendGrid](https://sendgrid.com/) account
2. Go to **Settings > API Keys**
3. Click **"Create API Key"**
4. Give the key a name (e.g., "Canva Builder Notification")
5. Select **"Full Access"** or **"Restricted Access"** with Mail Send enabled
6. Click **"Create & View"**
7. **Copy the API Key** (you won't be able to see it again!)

**Note**: SendGrid provides 100 free emails per day on the free plan.

## ?? Usage

### Method 1: Via Command

1. Open Cursor
2. Press `Cmd/Ctrl + Shift + P` to open Command Palette
3. Type `oneclick-publish` and select the command
4. Enter the required information:
   - **target_url**: Canva site URL (default: `https://muqtasr.my.canva.site/m3lem-suliman21436`)
   - **github_repo**: Repository name (default: `alzaem2002-ctrl/promptperfect`)
   - **github_token**: Your GitHub token
   - **notify_email**: Your email address
   - **sendgrid_key**: SendGrid API Key (leave empty if not needed)

### Method 2: Manual

1. Open the Agent from Cursor's Agents menu
2. Select **"?? Canva?Next.js One-Click Builder & Publisher"**
3. Enter all required information
4. Run the Agent

## ?? Required Inputs

| Input | Description | Default | Required |
|-------|-------------|---------|----------|
| `target_url` | Canva site URL to convert | `https://muqtasr.my.canva.site/m3lem-suliman21436` | ? |
| `github_repo` | Repository name (format: `owner/repo`) | `alzaem2002-ctrl/promptperfect` | ? |
| `github_token` | GitHub Personal Access Token | - | ? |
| `notify_email` | Email for notifications | `you@example.com` | ?? (if you want notifications) |
| `sendgrid_key` | SendGrid API Key for notifications | - | ? (optional) |

## ?? Outputs

After completion, a `publish.json` file will be created containing:

```json
{
  "release": "https://github.com/owner/repo/releases/tag/auto-2024-01-01",
  "zip": "https://github.com/owner/repo/releases/download/auto-2024-01-01/site-clone.zip",
  "site": "https://owner.github.io/repo/",
  "tag": "auto-2024-01-01"
}
```

## ?? What Happens During Execution

1. **Download Site**: All Canva site pages and files are downloaded
2. **Create Project**: A new Next.js project is created with Tailwind CSS
3. **Convert Pages**: Each HTML page is converted to a separate React component
4. **Setup RTL**: Arabic language support (RTL) is enabled with Tajawal font
5. **Compress**: The entire project is compressed into a ZIP file
6. **Upload**: The ZIP is uploaded to GitHub Releases
7. **Enable Pages**: GitHub Pages is automatically enabled
8. **Notify**: Email notification is sent (if SendGrid key is provided)

## ?? Important Notes

- Make sure the repository exists on GitHub before running
- GitHub Pages may take a few minutes to activate the site
- The ZIP file may be large depending on the Canva site size
- The process may take several minutes depending on site size

## ?? Troubleshooting

### GitHub Token Error
- Verify the token is correct and has required permissions
- Make sure the repository exists and you have write permissions

### SendGrid Error
- If email is not sent, verify the API key is correct
- Make sure email sending is enabled in SendGrid
- The process will complete even if email sending fails

### Canva Download Error
- Verify the URL is correct and accessible
- You may need to wait for all resources to download

## ?? Support

If you encounter issues, make sure:
- All prerequisites are installed (wget, zip, node, npx)
- Links and keys are correct
- You have an internet connection

## ?? License

This Agent is part of the Prompt Perfect project.

---

**Note**: This Agent automates a complex process. Make sure to review the generated code before final deployment.
