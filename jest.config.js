module.exports = {
	preset: 'ts-jest',
	testEnvironment: 'node',
	roots: ['src', '__tests__'],
	moduleFileExtensions: ['ts', 'tsx', 'js', 'jsx', 'json', 'node'],
	testMatch: [
		'**/__tests__/**/*.[jt]s?(x)',
		'**/?(*.)+(spec|test).[tj]s?(x)',
	],
	transform: {
		'^.+\\.(ts|tsx)$': 'ts-jest',
	},
	collectCoverageFrom: [
		'src/**/*.{ts,tsx}',
		'!src/**/*.d.ts',
		'!src/**/*.test.{ts,tsx}',
	],
	coverageDirectory: 'coverage',
	coverageReporters: ['text', 'lcov', 'json-summary'],
	coverageThresholds: {
		global: {
			lines: 80,
			functions: 80,
			branches: 75,
			statements: 80,
		},
	},
	maxWorkers: '50%', // Optimized by self-improving agent
};
