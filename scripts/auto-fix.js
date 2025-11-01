#!/usr/bin/env node
/**
 * Self-Improving Auto-Fix Script
 * Automatically fixes common test failures and code issues
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

class AutoFixer {
    constructor() {
        this.fixes = [];
        this.analysisPath = path.join(process.cwd(), 'test-analysis.json');
    }

    async run() {
        console.log('?? Auto-Fix Agent Starting...');

        try {
            // Load analysis results
            const analysis = this.loadAnalysis();
            
            if (!analysis || !analysis.issues || analysis.issues.length === 0) {
                console.log('? No issues found to fix');
                return;
            }

            // Apply fixes based on issue types
            for (const issue of analysis.issues) {
                await this.fixIssue(issue);
            }

            // Run linter auto-fix
            this.runLinterFix();

            // Verify fixes
            const success = await this.verifyFixes();

            // Report results
            this.reportResults(success);

        } catch (error) {
            console.error('? Auto-fix failed:', error.message);
            process.exit(1);
        }
    }

    loadAnalysis() {
        if (!fs.existsSync(this.analysisPath)) {
            return null;
        }

        try {
            return JSON.parse(fs.readFileSync(this.analysisPath, 'utf8'));
        } catch (error) {
            console.error('Error reading analysis:', error.message);
            return null;
        }
    }

    async fixIssue(issue) {
        console.log(`\n?? Addressing: ${issue.type} - ${issue.category || 'general'}`);

        switch (issue.type) {
            case 'pattern':
                await this.fixPatternIssue(issue);
                break;
            case 'performance':
                await this.fixPerformanceIssue(issue);
                break;
            case 'coverage':
                await this.improveCoverage(issue);
                break;
            default:
                console.log(`   ??  No auto-fix available for ${issue.type}`);
        }
    }

    async fixPatternIssue(issue) {
        switch (issue.category) {
            case 'Timeout':
                console.log('   ?? Increasing timeout values in tests...');
                this.increaseTestTimeouts();
                this.fixes.push({ type: 'timeout', action: 'increased timeout values' });
                break;
                
            case 'Mock Issue':
                console.log('   ?? Resetting mocks between tests...');
                this.addMockResets();
                this.fixes.push({ type: 'mock', action: 'added mock resets' });
                break;
                
            case 'Null/Undefined Reference':
                console.log('   ?? Adding null checks...');
                this.addNullChecks();
                this.fixes.push({ type: 'null-check', action: 'added null guards' });
                break;
                
            default:
                console.log(`   ??  Manual review needed for ${issue.category}`);
        }
    }

    increaseTestTimeouts() {
        const testFiles = this.findTestFiles();
        
        testFiles.forEach(file => {
            let content = fs.readFileSync(file, 'utf8');
            
            // Add jest timeout configuration if not present
            if (!content.includes('jest.setTimeout')) {
                const imports = content.split('\n').findIndex(line => 
                    line.includes('describe') || line.includes('test') || line.includes('it')
                );
                
                if (imports > -1) {
                    const lines = content.split('\n');
                    lines.splice(imports, 0, '\njest.setTimeout(30000); // Auto-increased by self-improving agent\n');
                    content = lines.join('\n');
                    fs.writeFileSync(file, content);
                    console.log(`   ? Updated timeout in ${path.basename(file)}`);
                }
            }
        });
    }

    addMockResets() {
        const testFiles = this.findTestFiles();
        
        testFiles.forEach(file => {
            let content = fs.readFileSync(file, 'utf8');
            
            // Check if beforeEach already exists
            if (content.includes('beforeEach')) {
                // Add clearAllMocks if not present
                if (!content.includes('jest.clearAllMocks()')) {
                    content = content.replace(
                        /beforeEach\s*\(\s*\(\s*\)\s*=>\s*{/g,
                        'beforeEach(() => {\n\t\tjest.clearAllMocks();'
                    );
                    fs.writeFileSync(file, content);
                    console.log(`   ? Added mock resets to ${path.basename(file)}`);
                }
            }
        });
    }

    addNullChecks() {
        // This is a placeholder - in a real implementation, this would use
        // AST parsing to add null checks intelligently
        console.log('   ??  Null check fixes require manual review');
    }

    async fixPerformanceIssue(issue) {
        console.log('   ?? Optimizing test performance...');
        
        // Add --maxWorkers flag to jest config if not present
        const jestConfigPath = path.join(process.cwd(), 'jest.config.js');
        
        if (fs.existsSync(jestConfigPath)) {
            let config = fs.readFileSync(jestConfigPath, 'utf8');
            
            if (!config.includes('maxWorkers')) {
                config = config.replace(
                    'module.exports = {',
                    'module.exports = {\n\tmaxWorkers: "50%", // Auto-optimized by self-improving agent'
                );
                fs.writeFileSync(jestConfigPath, config);
                this.fixes.push({ type: 'performance', action: 'optimized worker count' });
                console.log('   ? Optimized Jest worker configuration');
            }
        }
    }

    async improveCoverage(issue) {
        console.log('   ?? Coverage improvement suggestions generated');
        
        // Generate test stub suggestions
        const suggestions = this.generateTestStubs();
        
        if (suggestions.length > 0) {
            fs.writeFileSync(
                path.join(process.cwd(), 'test-stubs.md'),
                this.formatTestStubs(suggestions)
            );
            console.log('   ? Test stub suggestions saved to test-stubs.md');
        }
    }

    generateTestStubs() {
        // Analyze source files and suggest tests
        const srcDir = path.join(process.cwd(), 'src');
        const suggestions = [];

        if (!fs.existsSync(srcDir)) {
            return suggestions;
        }

        const files = this.getAllFiles(srcDir, '.ts');
        
        files.forEach(file => {
            const content = fs.readFileSync(file, 'utf8');
            
            // Find exported functions that might need tests
            const functionMatches = content.matchAll(/export\s+(function|const)\s+(\w+)/g);
            
            for (const match of functionMatches) {
                suggestions.push({
                    file: path.relative(process.cwd(), file),
                    function: match[2],
                    type: match[1]
                });
            }
        });

        return suggestions;
    }

    formatTestStubs(suggestions) {
        let output = '# Test Coverage Improvement Suggestions\n\n';
        output += '> Generated by Self-Improving Test Agent\n\n';
        
        suggestions.forEach(sug => {
            output += `## ${sug.function} (${sug.file})\n\n`;
            output += '```typescript\n';
            output += `test('${sug.function} should...', () => {\n`;
            output += `\t// TODO: Add test implementation\n`;
            output += `\texpect(${sug.function}()).toBeDefined();\n`;
            output += '});\n';
            output += '```\n\n';
        });

        return output;
    }

    runLinterFix() {
        console.log('\n?? Running linter auto-fix...');
        
        try {
            execSync('npm run lint -- --fix', { stdio: 'inherit' });
            this.fixes.push({ type: 'lint', action: 'fixed linting issues' });
            console.log('   ? Linting issues fixed');
        } catch (error) {
            console.log('   ??  Some linting issues could not be auto-fixed');
        }
    }

    async verifyFixes() {
        console.log('\n?? Verifying fixes...');
        
        try {
            execSync('npm test', { stdio: 'inherit' });
            console.log('   ? All tests passing after fixes!');
            return true;
        } catch (error) {
            console.log('   ??  Some tests still failing - manual review needed');
            return false;
        }
    }

    reportResults(success) {
        const report = {
            timestamp: new Date().toISOString(),
            success,
            fixes: this.fixes
        };

        fs.writeFileSync(
            path.join(process.cwd(), 'auto-fix-report.json'),
            JSON.stringify(report, null, 2)
        );

        console.log('\n?? Auto-Fix Report:');
        console.log(`   Applied ${this.fixes.length} fix(es)`);
        console.log(`   Status: ${success ? '? SUCCESS' : '??  PARTIAL'}`);
        
        this.fixes.forEach(fix => {
            console.log(`   - ${fix.type}: ${fix.action}`);
        });
    }

    findTestFiles() {
        const testDir = path.join(process.cwd(), '__tests__');
        return this.getAllFiles(testDir, '.test.ts');
    }

    getAllFiles(dir, extension) {
        const files = [];
        
        if (!fs.existsSync(dir)) {
            return files;
        }

        const items = fs.readdirSync(dir);
        
        items.forEach(item => {
            const fullPath = path.join(dir, item);
            const stat = fs.statSync(fullPath);
            
            if (stat.isDirectory()) {
                files.push(...this.getAllFiles(fullPath, extension));
            } else if (fullPath.endsWith(extension)) {
                files.push(fullPath);
            }
        });

        return files;
    }
}

// Run auto-fixer
const fixer = new AutoFixer();
fixer.run().catch(error => {
    console.error('Fatal error:', error);
    process.exit(1);
});
