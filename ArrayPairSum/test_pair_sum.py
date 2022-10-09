import pytest
import pair_sum as ps

TEST_CASES = [([1, 3, 2, 2], 4, [(1, 3), (2, 2)])]


@pytest.mark.parametrize('numbers, sum, expected', [(v[0], v[1], v[2]) for v in TEST_CASES])
def test_pair_sum(numbers: [], sum: int, expected: []) -> None:
    assert ps.pair_sum(numbers, sum) == expected
