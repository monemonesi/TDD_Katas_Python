import pytest
import random
import ValleyCounter


def test_count_valley_should_return_0_for_empty_path() -> None:
    """Test method initialisation"""
    assert ValleyCounter.count_valley(0, '') == 0


@pytest.mark.parametrize("steps", [random.randrange(0, 100)])
def test_count_valley_should_thrown_when_inputs_are_incorrect(steps) -> None:
    """Test method validation"""
    path = [random.choice(ValleyCounter.ALLOWED_PATH_I) for i in range(steps+2)]
    with pytest.raises(Exception) as e_info:
        ValleyCounter.count_valley(steps, path)


def test_update_high_for_step_correctly_update_high_when_up() -> None:
    """Test that the method update the hight as expected"""
    assert ValleyCounter.update_high_for_step(0, "U") == 1


def test_update_high_for_step_correctly_update_high_when_down() -> None:
    """Test that the method update the hight as expected"""
    assert ValleyCounter.update_high_for_step(0, "D") == -1


@pytest.mark.parametrize("valley_count", [random.randrange(0, 100)])
def test_update_valley_count_when_exiting_the_valley_should_add_to_the_count(valley_count: int) -> None:
    """Test that the method correctly add valley when the high is 0 and the previous high is < 0"""
    high = 0
    previous_high = -1
    assert ValleyCounter.update_valley_count(valley_count, high, previous_high) == valley_count + 1


@pytest.mark.parametrize("valley_count", [random.randrange(0, 100)])
def test_update_valley_count_when_high_is_not_zero_should_not_add_to_the_count(valley_count: int) -> None:
    """Test that the method correctly add valley when the high is 0 and the previous high is < 0"""
    high = [random.randrange(1, 100)]
    previous_high = -1
    assert ValleyCounter.update_valley_count(valley_count, high, previous_high)


@pytest.mark.parametrize("valley_count", [random.randrange(0, 100)])
def test_update_valley_count_when_exiting_the_valley_should_not_add_to_the_count(valley_count: int) -> None:
    """Test that the method correctly add valley when the high is 0 and the previous high is < 0"""
    high = 0
    previous_high = 1
    assert ValleyCounter.update_valley_count(valley_count, high, previous_high)


@pytest.mark.parametrize("partial_steps", [random.randrange(0, 20)])
def test_count_valley_should_return_1_when_path_has_only_down_followed_by_up(partial_steps) -> None:
    """Test result when path is composed by a series of downs followed by ups"""
    path = ''.join([ValleyCounter.DOWN for i in range(partial_steps)] + [ValleyCounter.UP for i in range(partial_steps)])
    assert ValleyCounter.count_valley(partial_steps*2, path) == 1


def test_count_valley_should_return_the_expected_output_1() -> None:
    """Test result when path is composed by a series of downs followed by ups"""
    path = "DDUUUUDD"
    assert ValleyCounter.count_valley(len(path), path) == 1


def test_count_valley_should_return_the_expected_output_2() -> None:
    """Test result when path is composed by a series of downs followed by ups"""
    path = "UDDDUDUU"
    assert ValleyCounter.count_valley(len(path), path) == 1