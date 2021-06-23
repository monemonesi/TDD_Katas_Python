import numpy as np


def make_jump(c: [], i: int, jumps: int) -> int:
    if c[i+2] == 0:
        return jumps+1, i+2
    else:
        return jumps+1, i+1


def jumpingOnClouds(c: []) -> int:
    """Function to calculate the minimum number of jump necessary to go from c0 to cn-1"""
    jumps = 0
    i = 0
    while i < len(c)-1:
        if i < len(c) - 2:
            jumps, i = make_jump(c, i, jumps)
        else:
            jumps += 1
            i += 1
    return jumps
