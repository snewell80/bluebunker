# Testing Guide for BlueBunker

This project uses pytest for testing. Here's how to run and write tests.

## Running Tests

### Basic Test Commands

```bash
# Activate virtual environment
source venv/bin/activate

# Run all tests
python -m pytest tests/ -v

# Run tests with coverage
python -m pytest tests/ --cov=src --cov-report=html -v

# Run only unit tests
python -m pytest tests/ -m unit -v

# Run tests excluding slow tests
python -m pytest tests/ -m "not slow" -v
```

### Using the Test Runner Script

```bash
# Make the script executable (if not already)
chmod +x run_tests.py

# Run all tests
python run_tests.py test

# Run tests with coverage
python run_tests.py test-cov

# Run only unit tests
python run_tests.py test-unit

# Run tests excluding slow tests
python run_tests.py test-fast
```

## Test Structure

```
tests/
├── __init__.py
├── test_config.py      # Tests for config module
├── test_enums.py       # Tests for enums module
└── test_userService.py # Tests for userService module
```

## Writing Tests

### Test File Naming
- Test files should start with `test_`
- Test classes should start with `Test`
- Test functions should start with `test_`

### Example Test Structure

```python
import pytest
from unittest.mock import Mock, patch
from your_module import your_function

class TestYourModule:
    def test_your_function_success(self):
        """Test successful case"""
        result = your_function("input")
        assert result == "expected_output"
    
    @patch('your_module.external_dependency')
    def test_your_function_with_mock(self, mock_dependency):
        """Test with mocked external dependency"""
        mock_dependency.return_value = "mocked_value"
        result = your_function("input")
        assert result == "expected_output"
```

### Test Markers

You can mark tests with different categories:

```python
@pytest.mark.unit
def test_unit_function():
    """Unit test"""
    pass

@pytest.mark.integration
def test_integration_function():
    """Integration test"""
    pass

@pytest.mark.slow
def test_slow_function():
    """Slow running test"""
    pass
```

## Coverage Reports

After running tests with coverage, you can view the HTML report:

```bash
# Generate coverage report
python -m pytest tests/ --cov=src --cov-report=html

# Open the report
open htmlcov/index.html
```

## Dependencies

Test dependencies are listed in `requirements.txt`:

- `pytest>=7.0.0` - Main testing framework
- `pytest-mock>=3.0.0` - Mocking utilities
- `pytest-cov>=4.0.0` - Coverage reporting
- `pytest-xdist>=3.0.0` - Parallel test execution (optional)

## Configuration

Pytest configuration is in `pytest.ini`:

- Test paths: `tests/`
- Test discovery patterns: `test_*.py`
- Verbose output by default
- Custom markers for test categorization
