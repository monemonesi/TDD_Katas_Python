import pytest
import anagram

TEST_CASES = [('dog', 'God', True), ('clint Eastwood', 'old west action', True), ('aa', 'ab', False),
              ('abc', 'abcdd', False)]


@pytest.mark.parametrize("s1, s2, expected", [(values[0], values[1], values[2]) for values in TEST_CASES])
def test_are_anagram_should_return_the_expected_value(s1: str, s2: str, expected: bool) -> None:
    """tested function return the expected result"""
    assert anagram.are_anagram(s1, s2) == expected


@pytest.mark.parametrize("s1, s2, expected", [(values[0], values[1], values[2]) for values in TEST_CASES])
def test_are_anagram_no_sort_should_return_the_expected_value(s1: str, s2: str, expected: bool) -> None:
    """tested function return the expected result"""
    assert anagram.are_anagram_no_sort(s1, s2) == expected
