#!/usr/bin/env node
/**
 * Improvement Suggestion Generator
 * Analyzes codebase and test failures to suggest improvements
 */

const fs = require('fs');
const path = require('path');

class ImprovementSuggester {
    constructor() {
        this.srcDir = path.join(process.cwd(), 'src');
        this.testDir = path.join(process.cwd(), '__tests__');
        this.suggestions = [];
    }

    async suggest() {
        console.log('?? Generating Improvement Suggestions...');

        try {
            // Analyze source code for new APIs
            const apis = await this.discoverAPIs();
            
            // Check for missing tests
            const missingTests = this.findMissingTests(apis);
            
            // Analyze test patterns
            const patterns = this.analyzeTestPatterns();
            
            // Generate suggestions
            this.generateSuggestions(apis, missingTests, patterns);
            
            // Output results
            this.outputSuggestions();
            
        } catch (error) {
            console.error('? Suggestion generation failed:', error.message);
            process.exit(1);
        }
    }

    async discoverAPIs() {
        const apis = [];

        if (!fs.existsSync(this.srcDir)) {
            return apis;
        }

        const files = this.getAllFiles(this.srcDir, '.ts');
        
        files.forEach(file => {
            const content = fs.readFileSync(file, 'utf8');
            const relativePath = path.relative(process.cwd(), file);
            
            // Find exported functions
            const functionMatches = content.matchAll(/export\s+(?:async\s+)?function\s+(\w+)/g);
            for (const match of functionMatches) {
                apis.push({
                    type: 'function',
                    name: match[1],
                    file: relativePath,
                    exported: true
                });
            }
            
            // Find exported classes
            const classMatches = content.matchAll(/export\s+class\s+(\w+)/g);
            for (const match of classMatches) {
                apis.push({
                    type: 'class',
                    name: match[1],
                    file: relativePath,
                    exported: true
                });
            }
            
            // Find exported constants
            const constMatches = content.matchAll(/export\s+const\s+(\w+)/g);
            for (const match of constMatches) {
                apis.push({
                    type: 'constant',
                    name: match[1],
                    file: relativePath,
                    exported: true
                });
            }
        });

        return apis;
    }

    findMissingTests(apis) {
        const missing = [];
        
        if (!fs.existsSync(this.testDir)) {
            return apis; // All APIs are missing tests
        }

        // Read all test files
        const testFiles = this.getAllFiles(this.testDir, '.test.ts');
        let allTestContent = '';
        testFiles.forEach(file => {
            allTestContent += fs.readFileSync(file, 'utf8');
        });

        // Check which APIs are not tested
        apis.forEach(api => {
            // Check if API name appears in tests
            const regex = new RegExp(`\\b${api.name}\\b`, 'g');
            const matches = allTestContent.match(regex);
            
            if (!matches || matches.length < 2) { // Less than 2 mentions (import + usage)
                missing.push(api);
            }
        });

        return missing;
    }

    analyzeTestPatterns() {
        const patterns = {
            hasBeforeEach: false,
            hasAfterEach: false,
            usesMocks: false,
            hasIntegrationTests: false,
            hasUnitTests: false,
            testCount: 0,
            describeBlocks: 0
        };

        if (!fs.existsSync(this.testDir)) {
            return patterns;
        }

        const testFiles = this.getAllFiles(this.testDir, '.test.ts');
        
        testFiles.forEach(file => {
            const content = fs.readFileSync(file, 'utf8');
            
            if (content.includes('beforeEach')) patterns.hasBeforeEach = true;
            if (content.includes('afterEach')) patterns.hasAfterEach = true;
            if (content.includes('jest.mock') || content.includes('.mock')) patterns.usesMocks = true;
            
            const testMatches = content.match(/\b(?:test|it)\s*\(/g);
            if (testMatches) patterns.testCount += testMatches.length;
            
            const describeMatches = content.match(/\bdescribe\s*\(/g);
            if (describeMatches) patterns.describeBlocks += describeMatches.length;
        });

        return patterns;
    }

    generateSuggestions(apis, missingTests, patterns) {
        // Missing test suggestions
        if (missingTests.length > 0) {
            this.suggestions.push({
                priority: 'high',
                category: 'Missing Tests',
                title: `Add tests for ${missingTests.length} untested API(s)`,
                details: missingTests.slice(0, 5).map(api => ({
                    api: `${api.type} ${api.name}`,
                    file: api.file,
                    testSuggestion: this.generateTestTemplate(api)
                }))
            });
        }

        // Test organization suggestions
        if (patterns.testCount > 10 && patterns.describeBlocks < 3) {
            this.suggestions.push({
                priority: 'medium',
                category: 'Test Organization',
                title: 'Organize tests into describe blocks',
                details: [{
                    suggestion: 'Group related tests using describe() blocks for better organization',
                    example: 'describe("Feature Name", () => { ... })'
                }]
            });
        }

        // Mock usage suggestions
        if (!patterns.usesMocks && apis.length > 5) {
            this.suggestions.push({
                priority: 'medium',
                category: 'Test Isolation',
                title: 'Consider using mocks for external dependencies',
                details: [{
                    suggestion: 'Use jest.mock() to isolate unit tests from external dependencies',
                    example: 'jest.mock("module-name")'
                }]
            });
        }

        // Cleanup suggestions
        if (!patterns.hasAfterEach && patterns.usesMocks) {
            this.suggestions.push({
                priority: 'low',
                category: 'Test Cleanup',
                title: 'Add cleanup in afterEach',
                details: [{
                    suggestion: 'Clean up mocks and state after each test',
                    example: 'afterEach(() => { jest.clearAllMocks(); })'
                }]
            });
        }

        // Test types suggestions
        this.suggestions.push({
            priority: 'low',
            category: 'Test Coverage Types',
            title: 'Consider adding different test types',
            details: [
                { type: 'Unit Tests', suggestion: 'Test individual functions in isolation' },
                { type: 'Integration Tests', suggestion: 'Test how components work together' },
                { type: 'Edge Cases', suggestion: 'Test boundary conditions and error handling' }
            ]
        });

        // API-specific suggestions
        if (apis.some(api => api.type === 'class')) {
            this.suggestions.push({
                priority: 'medium',
                category: 'Class Testing',
                title: 'Add comprehensive class tests',
                details: [{
                    suggestion: 'Test class methods, properties, and inheritance',
                    tests: [
                        'Constructor behavior',
                        'Method return values',
                        'State changes',
                        'Error handling'
                    ]
                }]
            });
        }
    }

    generateTestTemplate(api) {
        switch (api.type) {
            case 'function':
                return `
test('${api.name} should work correctly', () => {
    const result = ${api.name}(/* params */);
    expect(result).toBeDefined();
    // Add more assertions
});

test('${api.name} should handle edge cases', () => {
    // Test with null/undefined
    // Test with boundary values
    // Test error conditions
});`;

            case 'class':
                return `
describe('${api.name}', () => {
    let instance;
    
    beforeEach(() => {
        instance = new ${api.name}(/* params */);
    });
    
    test('should instantiate correctly', () => {
        expect(instance).toBeDefined();
    });
    
    test('should handle method calls', () => {
        // Test each public method
    });
});`;

            case 'constant':
                return `
test('${api.name} should have expected value', () => {
    expect(${api.name}).toBeDefined();
    // Add value assertions
});`;

            default:
                return `test('${api.name} test', () => { /* TODO */ });`;
        }
    }

    outputSuggestions() {
        if (this.suggestions.length === 0) {
            console.log('\n? No improvements needed - test suite looks good!');
            return;
        }

        console.log(`\n?? Generated ${this.suggestions.length} suggestion(s):\n`);

        this.suggestions.forEach((sug, idx) => {
            console.log(`${idx + 1}. [${sug.priority.toUpperCase()}] ${sug.category}`);
            console.log(`   ${sug.title}`);
        });

        // Generate markdown report
        let markdown = '# Test Suite Improvement Suggestions\n\n';
        markdown += `Generated: ${new Date().toISOString()}\n\n`;
        markdown += '---\n\n';

        this.suggestions.forEach((sug, idx) => {
            markdown += `## ${idx + 1}. ${sug.title}\n\n`;
            markdown += `**Category:** ${sug.category}  \n`;
            markdown += `**Priority:** ${sug.priority.toUpperCase()}\n\n`;
            
            if (sug.details) {
                markdown += '### Details\n\n';
                sug.details.forEach(detail => {
                    if (detail.api) {
                        markdown += `- **${detail.api}** (${detail.file})\n`;
                        if (detail.testSuggestion) {
                            markdown += '```typescript\n';
                            markdown += detail.testSuggestion.trim();
                            markdown += '\n```\n\n';
                        }
                    } else if (detail.suggestion) {
                        markdown += `- ${detail.suggestion}\n`;
                        if (detail.example) {
                            markdown += `  \`\`\`\n  ${detail.example}\n  \`\`\`\n`;
                        }
                    } else if (detail.type) {
                        markdown += `- **${detail.type}**: ${detail.suggestion}\n`;
                    }
                });
                markdown += '\n';
            }
        });

        fs.writeFileSync(
            path.join(process.cwd(), 'improvement-suggestions.md'),
            markdown
        );

        console.log('\n? Suggestions saved to improvement-suggestions.md');
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

// Run suggester
const suggester = new ImprovementSuggester();
suggester.suggest().catch(error => {
    console.error('Fatal error:', error);
    process.exit(1);
});
