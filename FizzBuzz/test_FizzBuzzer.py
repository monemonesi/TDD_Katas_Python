import pytest
import FizzBuzzer as FizzBuzzer


FIZZBUZZ_NUMBERS = [i for i in range(0, 100, 15)]
FIZZ_NUMBERS = [i for i in range(0, 100, 3) if i not in FIZZBUZZ_NUMBERS]
BUZZ_NUMBERS = [i for i in range(0, 100, 5) if i not in FIZZBUZZ_NUMBERS]
STANDARD_NUMBERS = [
    i
    for i in range(0, 100)
    if i not in FIZZBUZZ_NUMBERS and i not in FIZZ_NUMBERS and i not in BUZZ_NUMBERS
]


@pytest.mark.parametrize("test_input", [num for num in STANDARD_NUMBERS])
def test_get_value_return_standard_input(test_input: int) -> None:
    """When input are values not multiple of 3 nor 5 should return the input """
    assert FizzBuzzer.get_value(test_input) == f"{test_input}"


@pytest.mark.parametrize("test_input", [num for num in FIZZ_NUMBERS])
def test_get_value_should_return_Fizz_when_input_is_multiple_of_three(
    test_input: int,
) -> None:
    """When input values are multiple of three should return fizz"""
    assert FizzBuzzer.get_value(test_input) == "Fizz"


@pytest.mark.parametrize("test_input", [num for num in BUZZ_NUMBERS])
def test_get_value_should_return_Buzz_when_input_is_multiple_of_five(
    test_input: int,
) -> None:
    """When inputs are multiple of 5 should return Buzz"""
    assert FizzBuzzer.get_value(test_input) == "Buzz"


@pytest.mark.parametrize("test_input", [num for num in FIZZBUZZ_NUMBERS])
def test_get_value_should_return_Buzz_when_input_is_multiple_of_five(
    test_input: int,
) -> None:
    """When inputs are multiple of 5 should return Buzz"""
    assert FizzBuzzer.get_value(test_input) == "FizzBuzz"
