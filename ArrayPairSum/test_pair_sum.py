import pytest
import pair_sum as ps

TEST_CASES = [([1, 3, 2, 2], 4, {(1, 3), (2, 2)}), ([3, 1, 4, 0], 4, {(1, 3), (0, 4)})]


@pytest.mark.parametrize('numbers, sum, expected', [(v[0], v[1], v[2]) for v in TEST_CASES])
def test_pair_sum(numbers: [], sum: int, expected: []) -> None:
    assert ps.pair_sum(numbers, sum) == expected


@pytest.mark.parametrize('numbers, sum', [([1], 1), ([2], 1), ([], 1)])
def test_pair_sum_should_return_empty_when_array_len_less_than_two(numbers: [], sum: int) -> None:
    assert len(ps.pair_sum([1], 1)) == 0
