UP = "U"
DOWN = "D"
ALLOWED_PATH_I = [UP, DOWN]


def update_high_for_step(high: int, step: str) -> int:
    """Update the current high given a step"""
    if step == UP:
        high += 1
    elif step == DOWN:
        high -= 1
    return high


def update_valley_count(valleys_count: int, high: int, previous_high: int) -> int:
    if high == 0 and previous_high < 0:
        valleys_count += 1
    return valleys_count


def count_valley(steps: int, path: str) -> int:
    """Function which returns the number of valley encountered in a given path"""
    if len(path) != steps:
        raise Exception("Steps should match length of path")
    valleys = 0
    high = 0
    previous_high = 0
    for i in range(steps):
        previous_high = high
        high = update_high_for_step(high, path[i])
        valleys = update_valley_count(valleys, high, previous_high)

    return valleys
