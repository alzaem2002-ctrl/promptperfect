# Cursor Ultimate Prompt Guide

## Overview

Prompt Perfect is designed to streamline your workflow when using Cursor with LLM assistants. This guide provides the ultimate workflow for generating context-rich prompts.

## Quick Start

### Two Primary Commands

1. **Prompt Perfect: Open Editors**
   - Captures all currently open files
   - Generates a structured prompt with file contents
   - Perfect for focused code reviews or specific feature work

2. **Prompt Perfect: Open Editors and ASCII Tree**
   - Everything from "Open Editors"
   - Adds ASCII representation of your project structure
   - Ideal for architectural discussions or new contributor onboarding

## Optimal Workflow

### Step 1: Open Relevant Files
Open only the files relevant to your current task in Cursor. The extension will include these files in your prompt.

### Step 2: Configure Settings
Click the Prompt Perfect icon in the Activity Bar to configure:
- **Tree Depth Limit**: Default 4, adjust based on project complexity
- **Auto Copy to Clipboard**: Enabled by default for seamless pasting
- **Limit Prompt Length**: Optional token limiting
- **Additional Instructions**: Custom context for your LLM

### Step 3: Generate Your Prompt
Use the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`) and select:
- `Prompt Perfect: Open Editors` - For focused context
- `Prompt Perfect: Open Editors and ASCII Tree` - For structural context

### Step 4: Paste into Your LLM
The prompt is automatically copied to your clipboard and displayed in the OUTPUT panel. Paste directly into:
- Claude
- ChatGPT
- Cursor's AI chat
- Any other LLM interface

## Output Format

### File Content Format
```
\`\`\`path/to/file.ts
// File contents here
\`\`\`
```

### Tree Structure Format (when enabled)
```
\`\`\`Source Tree
project-root/
├── src/
│   ├── components/
│   └── utils/
└── tests/
\`\`\`
```

## Best Practices

### 1. Strategic File Selection
- Only open files directly relevant to your question
- Close unrelated tabs to avoid context pollution
- Use multiple prompts for different concerns rather than one massive prompt

### 2. Effective Additional Instructions
Default instruction: "If there is a file imported/included that I forgot to include or some other file you think I may have already created but have not included, please ask for that file before starting to generate a response."

Customize based on your needs:
- "Focus on TypeScript best practices"
- "Prioritize performance optimizations"
- "Suggest testing strategies"

### 3. Token Management
- Enable "Limit Prompt Length" for very large projects
- Set max tokens based on your LLM's context window:
  - GPT-4: ~8,000 tokens (safe limit)
  - GPT-4-32k: ~30,000 tokens
  - Claude 2: ~100,000 tokens
  - Claude 3: ~200,000 tokens

### 4. Tree Depth Optimization
- Small projects: 4-6 levels
- Large projects: 2-3 levels
- Monorepos: Use focused depth to avoid overwhelming structure

## Advanced Use Cases

### Code Review
1. Open all files in the PR/MR
2. Generate prompt with ASCII tree
3. Add instruction: "Review these changes for bugs, security issues, and best practices"

### Debugging
1. Open the problematic file and related imports
2. Generate prompt
3. Add instruction: "Help me debug this issue: [describe issue]"

### Architecture Planning
1. Open key architectural files
2. Generate with ASCII tree
3. Add instruction: "Suggest improvements to this architecture"

### Documentation Writing
1. Open the code files to document
2. Generate prompt
3. Add instruction: "Generate comprehensive documentation for these files"

## Troubleshooting

### Large File Warnings
If you see warnings about large files:
- Review whether the file is necessary for your question
- Consider breaking your question into smaller, focused prompts
- The extension warns at 1MB file size

### Token Limit Exceeded
If you hit token limits:
- Close some open files
- Reduce tree depth limit
- Split your task into multiple prompts
- Increase max token setting if your LLM supports it

### Files Not Appearing
Ensure:
- Files are actually open in editor tabs (not just in explorer)
- Files are within the workspace root
- Files aren't ignored by .gitignore (the extension respects gitignore)

## Integration with Cursor

Prompt Perfect was designed with Cursor in mind:
- Works seamlessly with Cursor's file handling
- Respects .gitignore for clean project structure
- Optimized for LLM-assisted coding workflows
- Complements Cursor's built-in AI features

## Tips for Maximum Effectiveness

1. **Start Small**: Begin with fewer files and expand as needed
2. **Iterate**: Generate multiple prompts as you refine your question
3. **Be Specific**: Use additional instructions to guide the LLM's focus
4. **Review Output**: Check the OUTPUT panel before pasting to verify context
5. **Version Control**: Keep prompt-related settings in your workspace config

## Example Workflows

### Adding a New Feature
```
1. Open: feature spec, related components, tests
2. Command: Open Editors and ASCII Tree
3. Instruction: "Help me implement [feature] following existing patterns"
```

### Refactoring
```
1. Open: files to refactor, related files
2. Command: Open Editors
3. Instruction: "Suggest refactoring to improve [concern]"
```

### Bug Investigation
```
1. Open: buggy file, test file, related utilities
2. Command: Open Editors
3. Instruction: "This produces [unexpected behavior]. Help me find the issue."
```

## Future Enhancements

The extension is actively developed. Planned features:
- Prompt history
- Custom templates
- More advanced token counting
- Diff-based prompts for code reviews

## Contributing

Found a bug or have a feature request? Contributions are welcome! This extension was built with LLM assistance and represents the future of collaborative coding.

---

*Remember: The best prompt is one that gives the LLM exactly the context it needs—no more, no less.*
