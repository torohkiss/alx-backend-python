#!/usr/bin/env python3
"""A module that does Complex types - mixed list"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ a type-annotated function sum_mixed_list which
    takes a list mxd_lst of integers and
    floats and returns their sum as a float."""

    summ: float = 0

    for i in mxd_lst:
        summ += i
    return summ
