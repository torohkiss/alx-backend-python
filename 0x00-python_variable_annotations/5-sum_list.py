#!/usr/bin/env python3
"""A module that sums Complex
types - list of floats"""


def sum_list(input_list: list[float]) -> float:
    summ: float = 0

    for x in input_list:
        summ += x
    return summ
