#!/usr/bin/env node
/**
 * Coverage Checker and Improvement Generator
 * Analyzes test coverage and suggests new tests
 */

const fs = require('fs');
const path = require('path');

class CoverageChecker {
    constructor() {
        this.coveragePath = path.join(process.cwd(), 'coverage', 'coverage-summary.json');
        this.thresholds = {
            lines: 80,
            statements: 80,
            functions: 80,
            branches: 75
        };
    }

    async check() {
        console.log('?? Coverage Checker Starting...');

        try {
            // Load coverage data
            const coverage = this.loadCoverage();
            
            if (!coverage) {
                console.log('??  No coverage data found');
                return;
            }

            // Check thresholds
            const issues = this.checkThresholds(coverage);
            
            // Find uncovered code
            const uncovered = this.findUncoveredCode(coverage);
            
            // Generate test suggestions
            const suggestions = this.generateSuggestions(uncovered);
            
            // Output report
            this.outputReport(coverage, issues, suggestions);
            
            // Exit with error if thresholds not met
            if (issues.length > 0) {
                console.log('\n? Coverage thresholds not met!');
                process.exit(1);
            }

            console.log('\n? All coverage thresholds met!');
            
        } catch (error) {
            console.error('? Coverage check failed:', error.message);
            process.exit(1);
        }
    }

    loadCoverage() {
        if (!fs.existsSync(this.coveragePath)) {
            return null;
        }

        try {
            return JSON.parse(fs.readFileSync(this.coveragePath, 'utf8'));
        } catch (error) {
            console.error('Error reading coverage:', error.message);
            return null;
        }
    }

    checkThresholds(coverage) {
        const issues = [];
        const total = coverage.total;

        Object.keys(this.thresholds).forEach(metric => {
            if (total[metric] && total[metric].pct < this.thresholds[metric]) {
                issues.push({
                    metric,
                    current: total[metric].pct,
                    threshold: this.thresholds[metric],
                    gap: this.thresholds[metric] - total[metric].pct
                });
            }
        });

        return issues;
    }

    findUncoveredCode(coverage) {
        const uncovered = [];

        Object.keys(coverage).forEach(file => {
            if (file === 'total') return;

            const fileCoverage = coverage[file];
            
            // Skip if coverage is good
            if (fileCoverage.lines.pct >= 90) return;

            uncovered.push({
                file: file.replace(process.cwd(), ''),
                lines: fileCoverage.lines.pct,
                functions: fileCoverage.functions.pct,
                branches: fileCoverage.branches.pct,
                statements: fileCoverage.statements.pct,
                uncoveredLines: this.extractUncoveredLines(fileCoverage)
            });
        });

        return uncovered.sort((a, b) => a.lines - b.lines);
    }

    extractUncoveredLines(fileCoverage) {
        const uncovered = [];
        
        if (fileCoverage.lines && fileCoverage.lines.uncovered) {
            // Parse uncovered line ranges
            const ranges = fileCoverage.lines.uncovered.split(',');
            ranges.forEach(range => {
                if (range.includes('-')) {
                    const [start, end] = range.split('-').map(Number);
                    uncovered.push({ start, end });
                } else {
                    const line = Number(range);
                    uncovered.push({ start: line, end: line });
                }
            });
        }

        return uncovered;
    }

    generateSuggestions(uncovered) {
        const suggestions = [];

        uncovered.forEach(file => {
            const priority = file.lines < 50 ? 'high' : file.lines < 70 ? 'medium' : 'low';
            
            suggestions.push({
                priority,
                file: file.file,
                currentCoverage: file.lines,
                recommendation: this.generateRecommendation(file),
                tests: this.suggestTests(file)
            });
        });

        return suggestions;
    }

    generateRecommendation(file) {
        if (file.lines < 50) {
            return 'Critical: Add comprehensive test coverage for this file';
        } else if (file.lines < 70) {
            return 'Add tests for uncovered branches and edge cases';
        } else {
            return 'Add tests for remaining uncovered lines';
        }
    }

    suggestTests(file) {
        const tests = [];

        // Suggest based on uncovered metrics
        if (file.branches < 70) {
            tests.push('Add tests for conditional branches (if/else, switch)');
        }
        
        if (file.functions < 80) {
            tests.push('Add tests for untested functions');
        }

        if (file.uncoveredLines.length > 0) {
            const totalUncovered = file.uncoveredLines.reduce((sum, range) => 
                sum + (range.end - range.start + 1), 0
            );
            
            if (totalUncovered > 10) {
                tests.push(`Add tests for ${totalUncovered} uncovered lines`);
            }
        }

        // Add error handling tests
        tests.push('Add error handling and edge case tests');

        return tests;
    }

    outputReport(coverage, issues, suggestions) {
        console.log('\n?? Coverage Report:');
        console.log('????????????????????????????????????????');

        // Overall coverage
        const total = coverage.total;
        console.log('\n?? Overall Coverage:');
        console.log(`   Lines:      ${total.lines.pct.toFixed(2)}% (${this.getStatus(total.lines.pct, this.thresholds.lines)})`);
        console.log(`   Statements: ${total.statements.pct.toFixed(2)}% (${this.getStatus(total.statements.pct, this.thresholds.statements)})`);
        console.log(`   Functions:  ${total.functions.pct.toFixed(2)}% (${this.getStatus(total.functions.pct, this.thresholds.functions)})`);
        console.log(`   Branches:   ${total.branches.pct.toFixed(2)}% (${this.getStatus(total.branches.pct, this.thresholds.branches)})`);

        // Threshold issues
        if (issues.length > 0) {
            console.log('\n??  Threshold Violations:');
            issues.forEach(issue => {
                console.log(`   ${issue.metric}: ${issue.current.toFixed(2)}% (need ${issue.threshold}%, gap: ${issue.gap.toFixed(2)}%)`);
            });
        }

        // Suggestions
        if (suggestions.length > 0) {
            console.log('\n?? Coverage Improvement Suggestions:');
            suggestions.slice(0, 5).forEach((sug, idx) => {
                console.log(`\n   ${idx + 1}. [${sug.priority.toUpperCase()}] ${sug.file}`);
                console.log(`      Current: ${sug.currentCoverage.toFixed(2)}%`);
                console.log(`      ${sug.recommendation}`);
                if (sug.tests.length > 0) {
                    console.log(`      Suggested tests:`);
                    sug.tests.forEach(test => {
                        console.log(`        - ${test}`);
                    });
                }
            });
        }

        // Save report
        const report = {
            timestamp: new Date().toISOString(),
            coverage: coverage.total,
            issues,
            suggestions
        };

        fs.writeFileSync(
            path.join(process.cwd(), 'coverage-report.json'),
            JSON.stringify(report, null, 2)
        );

        console.log('\n? Coverage report saved to coverage-report.json');
    }

    getStatus(current, threshold) {
        if (current >= threshold) {
            return '? PASS';
        } else if (current >= threshold - 5) {
            return '??  WARN';
        } else {
            return '? FAIL';
        }
    }
}

// Run checker
const checker = new CoverageChecker();
checker.check().catch(error => {
    console.error('Fatal error:', error);
    process.exit(1);
});
