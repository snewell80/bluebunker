#!/usr/bin/env python3
"""
Test runner script for bluebunker project.
This script provides an easy way to run tests with different configurations.
"""

import subprocess
import sys
import os


def run_command(cmd):
    """Run a command and return the result"""
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result


def main():
    """Main test runner function"""
    if len(sys.argv) > 1:
        command = sys.argv[1]
    else:
        command = "test"
    
    if command == "test":
        # Run all tests
        cmd = ["python", "-m", "pytest", "tests/", "-v"]
        result = run_command(cmd)
    elif command == "test-cov":
        # Run tests with coverage
        cmd = ["python", "-m", "pytest", "tests/", "--cov=src", "--cov-report=html", "-v"]
        result = run_command(cmd)
    elif command == "test-fast":
        # Run tests without slow tests
        cmd = ["python", "-m", "pytest", "tests/", "-m", "not slow", "-v"]
        result = run_command(cmd)
    elif command == "test-unit":
        # Run only unit tests
        cmd = ["python", "-m", "pytest", "tests/", "-m", "unit", "-v"]
        result = run_command(cmd)
    else:
        print("Available commands:")
        print("  test       - Run all tests")
        print("  test-cov   - Run tests with coverage report")
        print("  test-fast  - Run tests excluding slow tests")
        print("  test-unit - Run only unit tests")
        return
    
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
