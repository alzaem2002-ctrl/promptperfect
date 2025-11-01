# ?? Self-Improving Test Agent - Quick Start

## What is This?

This project now includes an AI-powered self-improving test system that:
- ? Monitors tests automatically every hour
- ?? Auto-fixes common failures
- ? Optimizes performance
- ?? Improves coverage
- ?? Suggests new tests
- ?? Creates detailed reports

## Quick Commands

```bash
# Run the complete self-improvement cycle
npm run test:self-improve

# Run individual tools
npm run test:coverage          # Run tests with coverage
npm run test:analyze          # Analyze test results
npm run test:performance      # Check performance
npm run test:suggest          # Get improvement suggestions
npm run test:report           # Generate full report
npm run test:fix              # Auto-fix issues
```

## GitHub Actions

The system runs automatically:
- ? On every push
- ? On pull requests  
- ? Every hour (scheduled)
- ? Manual trigger available

View results in the **Actions** tab!

## What It Does Automatically

### 1. Monitors Tests ??
- Tracks pass/fail rates
- Detects failure patterns
- Identifies flaky tests

### 2. Auto-Fixes Issues ??
- Timeout problems
- Mock configuration
- Linting errors
- Performance issues

### 3. Improves Coverage ??
- Finds untested code
- Generates test stubs
- Suggests edge cases

### 4. Optimizes Performance ?
- Identifies slow tests
- Suggests parallelization
- Recommends caching

### 5. Reports Everything ??
- PR comments
- GitHub issues
- Detailed reports

## Files Generated

After running, check these files:
- `improvement-report.md` - Main report
- `improvement-suggestions.md` - Specific suggestions
- `test-analysis.json` - Test metrics
- `performance-report.json` - Performance data
- `coverage-report.json` - Coverage analysis

## Configuration

### Coverage Thresholds
Edit `scripts/check-coverage.js`:
```javascript
lines: 80,      // 80% line coverage required
functions: 80,  // 80% function coverage required
branches: 75    // 75% branch coverage required
```

### Schedule Frequency
Edit `.github/workflows/self-improving-tests.yml`:
```yaml
schedule:
  - cron: '0 * * * *'  # Every hour
  # Change to '0 */6 * * *' for every 6 hours
```

## Example Workflow

1. **Write Code** ? Push to GitHub
2. **Agent Runs** ? Analyzes tests automatically
3. **Get Report** ? Check PR comments
4. **Review** ? Look at generated reports
5. **Apply** ? Use suggested improvements
6. **Repeat** ? System learns and improves!

## Common Use Cases

### After Adding New Feature
```bash
npm run test:suggest
```
? Get test suggestions for your new code

### Before PR
```bash
npm run test:self-improve
```
? Full analysis and report

### Debugging Slow Tests
```bash
npm run test:performance
```
? Find bottlenecks

### Fixing Failing Tests
```bash
npm run test:fix
```
? Attempt automatic fixes

## Reports Explained

### improvement-report.md
**What**: Comprehensive overview
**When**: After full analysis
**Action**: Review all sections

### improvement-suggestions.md
**What**: Specific test suggestions with templates
**When**: When coverage is low
**Action**: Copy/paste test templates

### test-analysis.json
**What**: Raw metrics and patterns
**When**: Debugging test issues
**Action**: Check failure patterns

### performance-report.json
**What**: Performance metrics and trends
**When**: Tests are slow
**Action**: Apply optimization suggestions

## Tips & Tricks

### ?? Focus on High Priority
Start with `[HIGH]` priority items in reports

### ?? Watch the Trends
Performance degrading? Act quickly!

### ?? Let It Run
Don't disable the hourly checks - that's when magic happens

### ?? Review Before Applying
Always check what was auto-fixed:
```bash
git diff
```

### ?? Optimize CI
Use the caching strategies suggested in reports

## Troubleshooting

### "No test results found"
Run tests with coverage first:
```bash
npm run test:coverage
```

### "Scripts not executable"
```bash
chmod +x scripts/*.js
```

### "GitHub Actions failing"
Check the Actions tab for logs

### "Auto-fix didn't work"
Some issues need manual intervention - check the report

## What It Does NOT Do

? Does not commit automatically
? Does not push to GitHub
? Does not modify source code (only tests)
? Does not create PRs (only issues)
? Does not run without approval on main

## Learn More

Full documentation: `devdocs/self-improving-tests.md`

## Status Dashboard

Check system health:
```bash
# View historical data
ls -la .test-history/
ls -la .performance-metrics/

# Check latest report
cat improvement-report.md
```

## Need Help?

1. Read `devdocs/self-improving-tests.md`
2. Check generated reports
3. Review GitHub Actions logs
4. Create an issue

---

**Happy Testing! ??**

The agent is working in the background, continuously improving your test suite.

*Last Updated: 2025-11-01*
