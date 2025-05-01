# FDE Technical Screen Solution

This repository contains my solution to the FDE Technical Screen challenge. It demonstrates a robust, tested implementation of a package classification function using Pydantic for validation and Pytest for automated testing.

## Repository Structure

```plaintext
├── factory_sort.py        # Core implementation of the `sort` function
├── test_factory_sort.py   # Pytest suite covering valid and invalid scenarios
└── README.md              # This documentation file
```

## Requirements

- Python 3.8 or higher
- [Pydantic](https://pydantic-docs.helpmanual.io/) (for data validation)
- [Pytest](https://docs.pytest.org/) (for running the test suite)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/davidye007/ThoughtfulAI
   cd ThoughtfulAI
   ```

2. Install dependencies:
   ```bash
   pip install pydantic pytest
   ```

## Usage

Import and call the `sort` function from `factory_sort.py`:

```python
from factory_sort import sort

# Example:
label = sort(width=10, height=20, length=30, mass=5)
print(label)  # Output: "STANDARD", "SPECIAL", or "REJECTED"
```

### Classification Logic

- **STANDARD**: Not bulky *and* not heavy
- **SPECIAL**: Bulky *or* heavy (but not both)
- **REJECTED**: Both bulky *and* heavy

Thresholds are defined as constants in `factory_sort.py`:
```python
BULKY_VOL_CM3 = 1000000   # Volume threshold in cubic cm
BULKY_DIM_CM  = 150         # Maximum single dimension in cm
HEAVY_KG      = 20          # Mass threshold in kg
```

## Running Tests

Execute the test suite with Pytest:

```bash
pytest -q
```

You should see all tests pass, covering:

- Standard, Special, and Rejected classifications
- Edge cases at threshold boundaries
- Validation errors for negative or non-numeric inputs

---


