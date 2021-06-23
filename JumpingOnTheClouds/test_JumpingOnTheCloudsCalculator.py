import pytest
import numpy as np
import JumpingOnTheCloudsCalculator as Calculator

FIVE_CLOUDS_PATHS = np.array([[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 0, 0]])
FIVE_CLOUDS_EXPECTED_RESULTS = np.array([2, 3, 2])
FIVE_CLOUDS_PATHS_RESULT = [([0, 0, 0, 0, 0], 2), ([0, 0, 1, 0, 0], 3), ([0, 1, 0, 0, 0], 2)]


@pytest.mark.parametrize("c, expected", [([0, 0, 0], (1, 2)), ([0, 0, 1], (1, 1))])
def test_make_jump_should_increment_jumps_and_index_correctly(c, expected) -> None:
    """Test the make_jump helper function"""
    assert Calculator.make_jump(c, 0, 0) == expected


def test_jumpingOnClouds_should_return_2_with_4_green_clouds() -> None:
    """Test path with 4 greens clouds"""
    assert Calculator.jumpingOnClouds([0, 0, 0, 0]) == 2


def test_jumpingOnClouds_return_the_correct_input_when_5_clouds() -> None:
    assert Calculator.jumpingOnClouds([0, 0, 1, 0, 0]) == 3


@pytest.mark.parametrize('path_result', [t for t in FIVE_CLOUDS_PATHS_RESULT])
def test_jumpingOnClouds_return_the_correct_input_when_5_clouds(path_result: ()) -> None:
    assert Calculator.jumpingOnClouds(path_result[0]) == path_result[1]
