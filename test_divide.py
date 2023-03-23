import pytest
from divide import divide_numbers


def test_divide_when_other_number_is_zero_raises_an_exception():
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        divide_numbers(2, 0)
