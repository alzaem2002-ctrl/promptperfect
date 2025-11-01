#!/usr/bin/env node
/**
 * Performance Monitoring Script
 * Tracks test execution performance and suggests optimizations
 */

const fs = require('fs');
const path = require('path');

class PerformanceMonitor {
    constructor() {
        this.metricsPath = path.join(process.cwd(), '.performance-metrics');
        this.thresholds = {
            testDuration: 1000, // 1 second per test
            totalDuration: 30000, // 30 seconds total
            memoryUsage: 512 * 1024 * 1024, // 512MB
        };
    }

    async monitor() {
        console.log('? Performance Monitor Starting...');

        try {
            // Collect current metrics
            const metrics = await this.collectMetrics();
            
            // Compare with historical data
            const trends = this.analyzeTrends(metrics);
            
            // Identify bottlenecks
            const bottlenecks = this.identifyBottlenecks(metrics);
            
            // Generate optimization suggestions
            const suggestions = this.generateSuggestions(metrics, trends, bottlenecks);
            
            // Save metrics
            this.saveMetrics(metrics);
            
            // Output report
            this.outputReport(metrics, trends, bottlenecks, suggestions);
            
        } catch (error) {
            console.error('? Performance monitoring failed:', error.message);
            process.exit(1);
        }
    }

    async collectMetrics() {
        const metrics = {
            timestamp: new Date().toISOString(),
            testDuration: 0,
            averageTestTime: 0,
            slowestTests: [],
            memoryUsage: process.memoryUsage(),
            cpuUsage: process.cpuUsage(),
        };

        // Try to read test results
        const testResultsPath = path.join(process.cwd(), 'test-results.json');
        if (fs.existsSync(testResultsPath)) {
            const results = JSON.parse(fs.readFileSync(testResultsPath, 'utf8'));
            
            if (results.testResults) {
                let totalDuration = 0;
                let testCount = 0;
                const slowTests = [];

                results.testResults.forEach(suite => {
                    suite.assertionResults?.forEach(test => {
                        if (test.duration) {
                            totalDuration += test.duration;
                            testCount++;

                            if (test.duration > this.thresholds.testDuration) {
                                slowTests.push({
                                    name: test.title,
                                    duration: test.duration,
                                    file: suite.name
                                });
                            }
                        }
                    });
                });

                metrics.testDuration = totalDuration;
                metrics.averageTestTime = testCount > 0 ? totalDuration / testCount : 0;
                metrics.slowestTests = slowTests.sort((a, b) => b.duration - a.duration).slice(0, 5);
            }
        }

        return metrics;
    }

    analyzeTrends(currentMetrics) {
        const trends = {
            performance: 'stable',
            direction: null,
            change: 0
        };

        // Load historical metrics
        const history = this.loadHistory();
        
        if (history.length < 2) {
            return trends;
        }

        // Compare with previous run
        const previous = history[history.length - 2];
        
        if (previous.testDuration && currentMetrics.testDuration) {
            const change = ((currentMetrics.testDuration - previous.testDuration) / previous.testDuration) * 100;
            trends.change = change;

            if (Math.abs(change) < 5) {
                trends.performance = 'stable';
                trends.direction = null;
            } else if (change > 0) {
                trends.performance = 'degrading';
                trends.direction = 'slower';
            } else {
                trends.performance = 'improving';
                trends.direction = 'faster';
            }
        }

        return trends;
    }

    identifyBottlenecks(metrics) {
        const bottlenecks = [];

        // Check test duration
        if (metrics.testDuration > this.thresholds.totalDuration) {
            bottlenecks.push({
                type: 'duration',
                severity: 'high',
                message: `Total test duration (${metrics.testDuration}ms) exceeds threshold (${this.thresholds.totalDuration}ms)`,
                impact: 'CI/CD pipeline slowdown'
            });
        }

        // Check average test time
        if (metrics.averageTestTime > this.thresholds.testDuration) {
            bottlenecks.push({
                type: 'avg-duration',
                severity: 'medium',
                message: `Average test time (${metrics.averageTestTime.toFixed(2)}ms) exceeds threshold`,
                impact: 'Individual test performance'
            });
        }

        // Check for slow tests
        if (metrics.slowestTests.length > 0) {
            bottlenecks.push({
                type: 'slow-tests',
                severity: 'medium',
                message: `${metrics.slowestTests.length} slow test(s) detected`,
                impact: 'Test suite performance',
                details: metrics.slowestTests
            });
        }

        // Check memory usage
        const heapUsed = metrics.memoryUsage.heapUsed;
        if (heapUsed > this.thresholds.memoryUsage) {
            bottlenecks.push({
                type: 'memory',
                severity: 'medium',
                message: `High memory usage: ${(heapUsed / 1024 / 1024).toFixed(2)}MB`,
                impact: 'Resource consumption'
            });
        }

        return bottlenecks;
    }

    generateSuggestions(metrics, trends, bottlenecks) {
        const suggestions = [];

        // Suggest parallelization
        if (metrics.testDuration > 10000) {
            suggestions.push({
                priority: 'high',
                category: 'parallelization',
                action: 'Enable parallel test execution with --maxWorkers',
                implementation: 'Update jest.config.js: maxWorkers: "50%"',
                expectedImprovement: '30-50% faster'
            });
        }

        // Suggest test splitting
        if (metrics.slowestTests.length > 3) {
            suggestions.push({
                priority: 'high',
                category: 'optimization',
                action: 'Split slow tests into smaller units',
                implementation: 'Break down integration tests into unit tests',
                expectedImprovement: '20-40% faster'
            });
        }

        // Suggest caching
        if (trends.performance === 'degrading') {
            suggestions.push({
                priority: 'medium',
                category: 'caching',
                action: 'Implement test result caching',
                implementation: 'Use jest --cache and GitHub Actions cache',
                expectedImprovement: '15-25% faster on repeated runs'
            });
        }

        // Suggest mocking optimization
        if (bottlenecks.some(b => b.type === 'slow-tests')) {
            suggestions.push({
                priority: 'medium',
                category: 'mocking',
                action: 'Review and optimize mock implementations',
                implementation: 'Use jest.mock() efficiently, avoid unnecessary mock resets',
                expectedImprovement: '10-20% faster'
            });
        }

        // Memory optimization
        if (bottlenecks.some(b => b.type === 'memory')) {
            suggestions.push({
                priority: 'medium',
                category: 'memory',
                action: 'Optimize memory usage in tests',
                implementation: 'Clear large objects, use afterEach cleanup',
                expectedImprovement: 'Reduced memory footprint'
            });
        }

        return suggestions;
    }

    loadHistory() {
        if (!fs.existsSync(this.metricsPath)) {
            return [];
        }

        const files = fs.readdirSync(this.metricsPath)
            .filter(f => f.endsWith('.json'))
            .sort()
            .slice(-30); // Keep last 30 entries

        return files.map(file => {
            const content = fs.readFileSync(path.join(this.metricsPath, file), 'utf8');
            return JSON.parse(content);
        });
    }

    saveMetrics(metrics) {
        if (!fs.existsSync(this.metricsPath)) {
            fs.mkdirSync(this.metricsPath, { recursive: true });
        }

        const filename = `metrics-${Date.now()}.json`;
        fs.writeFileSync(
            path.join(this.metricsPath, filename),
            JSON.stringify(metrics, null, 2)
        );
    }

    outputReport(metrics, trends, bottlenecks, suggestions) {
        console.log('\n?? Performance Report:');
        console.log('????????????????????????????????????????');
        
        // Current metrics
        console.log('\n?? Current Metrics:');
        console.log(`   Total Duration: ${metrics.testDuration}ms`);
        console.log(`   Average Test: ${metrics.averageTestTime.toFixed(2)}ms`);
        console.log(`   Memory (Heap): ${(metrics.memoryUsage.heapUsed / 1024 / 1024).toFixed(2)}MB`);
        
        // Trends
        if (trends.direction) {
            console.log('\n?? Performance Trend:');
            console.log(`   Status: ${trends.performance} (${trends.change.toFixed(2)}% ${trends.direction})`);
        }

        // Bottlenecks
        if (bottlenecks.length > 0) {
            console.log('\n??  Bottlenecks Detected:');
            bottlenecks.forEach(b => {
                console.log(`   [${b.severity.toUpperCase()}] ${b.message}`);
                if (b.details) {
                    b.details.slice(0, 3).forEach(d => {
                        console.log(`      - ${d.name}: ${d.duration}ms`);
                    });
                }
            });
        }

        // Suggestions
        if (suggestions.length > 0) {
            console.log('\n?? Optimization Suggestions:');
            suggestions.forEach((sug, idx) => {
                console.log(`\n   ${idx + 1}. [${sug.priority.toUpperCase()}] ${sug.category}`);
                console.log(`      Action: ${sug.action}`);
                console.log(`      How: ${sug.implementation}`);
                console.log(`      Impact: ${sug.expectedImprovement}`);
            });
        }

        // Save report
        const report = {
            timestamp: new Date().toISOString(),
            metrics,
            trends,
            bottlenecks,
            suggestions
        };

        fs.writeFileSync(
            path.join(process.cwd(), 'performance-report.json'),
            JSON.stringify(report, null, 2)
        );

        console.log('\n? Performance report saved to performance-report.json');
    }
}

// Run monitor
const monitor = new PerformanceMonitor();
monitor.monitor().catch(error => {
    console.error('Fatal error:', error);
    process.exit(1);
});
