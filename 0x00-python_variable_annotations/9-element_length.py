#!/usr/bin/env python3
"""Let's duck type an iterable object"""

from typing import Tuple, List, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotating the below function’s parameters
    and returning values with the appropriate types"""

    return [(i, len(i)) for i in lst]
