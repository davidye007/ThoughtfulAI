import pytest
from pydantic import ValidationError
from factory_sort import sort

# valid classification scenarios: (dimensions, mass, expected_label)
VALID_CASES = [
    ((10, 10, 10), 5, 'STANDARD'),          # neither bulky nor heavy
    ((200, 1, 1), 5, 'SPECIAL'),            # bulky only (volume)
    ((10, 10, 10), 20.5, 'SPECIAL'),        # heavy only (mass)
    ((151, 0, 0), 25, 'REJECTED'),          # both bulky & heavy
    ((100, 100, 100), 0, 'STANDARD'),       # edge: volume == 1_000_000
    ((100, 100, 100.1), 0, 'SPECIAL'),      # edge: volume > 1_000_000
    ((150, 1, 1), 0, 'SPECIAL'),            # edge: max dimension == 150
    ((150.1, 1, 1), 0, 'SPECIAL'),          # edge: max dimension > 150
    ((1, 1, 1), 20, 'SPECIAL'),             # edge: mass == 20
]

@pytest.mark.parametrize("dims, mass, expected", VALID_CASES)
def test_sort_classification_valid(dims, mass, expected):
    """
    sort() should return the correct category label for valid inputs.
    """
    width, height, length = dims
    result = sort(width, height, length, mass)
    assert result == expected

# invalid input scenarios: negative or non-numeric values should raise
INVALID_ARGS = [
    (-1, 10, 10, 5),             # negative dimension
    ('foo', 10, 10, 5),          # non-numeric width
    (10, None, 10, 5),           # missing height
]

@pytest.mark.parametrize("args", INVALID_ARGS)
def test_sort_invalid_input_raises_validation_error(args):
    """
    sort() should raise ValidationError for invalid inputs.
    """
    with pytest.raises(ValidationError):
        sort(*args)
