#!/usr/bin/env node
/**
 * Self-Improving Test Analyzer
 * Monitors test results and identifies patterns, issues, and improvement opportunities
 */

const fs = require('fs');
const path = require('path');

class TestAnalyzer {
    constructor() {
        this.testResultsPath = path.join(process.cwd(), 'test-results.json');
        this.historyPath = path.join(process.cwd(), '.test-history');
        this.issues = [];
        this.metrics = {
            totalTests: 0,
            passedTests: 0,
            failedTests: 0,
            skippedTests: 0,
            duration: 0,
            coverage: null
        };
    }

    async analyze() {
        console.log('?? Analyzing test results...');
        
        try {
            // Load test results
            const results = this.loadTestResults();
            if (!results) {
                console.log('??  No test results found');
                return;
            }

            // Analyze test metrics
            this.analyzeMetrics(results);
            
            // Check for patterns in failures
            this.detectFailurePatterns(results);
            
            // Analyze test performance
            this.analyzePerformance(results);
            
            // Check test coverage
            await this.analyzeCoverage();
            
            // Store history for trend analysis
            this.updateHistory();
            
            // Generate recommendations
            this.generateRecommendations();
            
            // Output results
            this.outputResults();
            
        } catch (error) {
            console.error('? Error analyzing tests:', error.message);
            process.exit(1);
        }
    }

    loadTestResults() {
        if (!fs.existsSync(this.testResultsPath)) {
            return null;
        }
        
        try {
            const content = fs.readFileSync(this.testResultsPath, 'utf8');
            return JSON.parse(content);
        } catch (error) {
            console.error('Error reading test results:', error.message);
            return null;
        }
    }

    analyzeMetrics(results) {
        if (results.numTotalTests !== undefined) {
            this.metrics.totalTests = results.numTotalTests;
            this.metrics.passedTests = results.numPassedTests || 0;
            this.metrics.failedTests = results.numFailedTests || 0;
            this.metrics.skippedTests = results.numPendingTests || 0;
        }

        console.log(`\n?? Test Metrics:`);
        console.log(`   Total: ${this.metrics.totalTests}`);
        console.log(`   ? Passed: ${this.metrics.passedTests}`);
        console.log(`   ? Failed: ${this.metrics.failedTests}`);
        console.log(`   ??  Skipped: ${this.metrics.skippedTests}`);
    }

    detectFailurePatterns(results) {
        if (!results.testResults) return;

        const failurePatterns = new Map();
        
        results.testResults.forEach(testFile => {
            testFile.assertionResults?.forEach(test => {
                if (test.status === 'failed') {
                    const errorType = this.categorizeError(test.failureMessages);
                    failurePatterns.set(errorType, (failurePatterns.get(errorType) || 0) + 1);
                }
            });
        });

        if (failurePatterns.size > 0) {
            console.log('\n?? Failure Patterns Detected:');
            failurePatterns.forEach((count, pattern) => {
                console.log(`   ${pattern}: ${count} occurrence(s)`);
                this.issues.push({
                    type: 'pattern',
                    category: pattern,
                    count: count,
                    severity: count > 3 ? 'high' : 'medium'
                });
            });
        }
    }

    categorizeError(failureMessages) {
        if (!failureMessages || failureMessages.length === 0) {
            return 'Unknown Error';
        }

        const message = failureMessages.join(' ');
        
        if (message.includes('timeout') || message.includes('Timeout')) {
            return 'Timeout';
        } else if (message.includes('mock') || message.includes('Mock')) {
            return 'Mock Issue';
        } else if (message.includes('undefined') || message.includes('null')) {
            return 'Null/Undefined Reference';
        } else if (message.includes('expect')) {
            return 'Assertion Failure';
        } else if (message.includes('import') || message.includes('require')) {
            return 'Module Import Issue';
        } else {
            return 'Logic Error';
        }
    }

    analyzePerformance(results) {
        if (!results.testResults) return;

        const slowTests = [];
        const performanceThreshold = 5000; // 5 seconds

        results.testResults.forEach(testFile => {
            testFile.assertionResults?.forEach(test => {
                if (test.duration && test.duration > performanceThreshold) {
                    slowTests.push({
                        name: test.title,
                        duration: test.duration,
                        file: testFile.name
                    });
                }
            });
        });

        if (slowTests.length > 0) {
            console.log('\n??  Slow Tests Detected:');
            slowTests.forEach(test => {
                console.log(`   ${test.name}: ${test.duration}ms`);
                this.issues.push({
                    type: 'performance',
                    test: test.name,
                    duration: test.duration,
                    severity: 'medium'
                });
            });
        }
    }

    async analyzeCoverage() {
        const coveragePath = path.join(process.cwd(), 'coverage', 'coverage-summary.json');
        
        if (!fs.existsSync(coveragePath)) {
            console.log('\n??  No coverage data found');
            return;
        }

        try {
            const coverage = JSON.parse(fs.readFileSync(coveragePath, 'utf8'));
            this.metrics.coverage = coverage.total;

            console.log('\n?? Coverage Metrics:');
            console.log(`   Lines: ${coverage.total.lines.pct}%`);
            console.log(`   Statements: ${coverage.total.statements.pct}%`);
            console.log(`   Functions: ${coverage.total.functions.pct}%`);
            console.log(`   Branches: ${coverage.total.branches.pct}%`);

            // Check if coverage is below threshold
            if (coverage.total.lines.pct < 80) {
                this.issues.push({
                    type: 'coverage',
                    metric: 'lines',
                    current: coverage.total.lines.pct,
                    target: 80,
                    severity: 'medium'
                });
            }
        } catch (error) {
            console.error('Error reading coverage:', error.message);
        }
    }

    updateHistory() {
        if (!fs.existsSync(this.historyPath)) {
            fs.mkdirSync(this.historyPath, { recursive: true });
        }

        const timestamp = new Date().toISOString();
        const historyEntry = {
            timestamp,
            metrics: this.metrics,
            issues: this.issues
        };

        const historyFile = path.join(this.historyPath, `${timestamp.split('T')[0]}.json`);
        
        let history = [];
        if (fs.existsSync(historyFile)) {
            history = JSON.parse(fs.readFileSync(historyFile, 'utf8'));
        }
        
        history.push(historyEntry);
        fs.writeFileSync(historyFile, JSON.stringify(history, null, 2));
    }

    generateRecommendations() {
        const recommendations = [];

        // Check for duplicate tests
        if (this.issues.some(i => i.type === 'pattern' && i.count > 2)) {
            recommendations.push({
                priority: 'high',
                action: 'Review duplicate test failures - may indicate systemic issue',
                category: 'reliability'
            });
        }

        // Check for performance issues
        if (this.issues.some(i => i.type === 'performance')) {
            recommendations.push({
                priority: 'medium',
                action: 'Optimize slow tests or split into smaller units',
                category: 'performance'
            });
        }

        // Check coverage
        if (this.metrics.coverage && this.metrics.coverage.lines.pct < 80) {
            recommendations.push({
                priority: 'medium',
                action: 'Increase test coverage by adding tests for uncovered code paths',
                category: 'coverage'
            });
        }

        if (recommendations.length > 0) {
            console.log('\n?? Recommendations:');
            recommendations.forEach(rec => {
                console.log(`   [${rec.priority.toUpperCase()}] ${rec.action}`);
            });
        }

        this.recommendations = recommendations;
    }

    outputResults() {
        const report = {
            timestamp: new Date().toISOString(),
            metrics: this.metrics,
            issues: this.issues,
            recommendations: this.recommendations || []
        };

        fs.writeFileSync(
            path.join(process.cwd(), 'test-analysis.json'),
            JSON.stringify(report, null, 2)
        );

        console.log('\n? Analysis complete! Report saved to test-analysis.json');
    }
}

// Run analyzer
const analyzer = new TestAnalyzer();
analyzer.analyze().catch(error => {
    console.error('Fatal error:', error);
    process.exit(1);
});
