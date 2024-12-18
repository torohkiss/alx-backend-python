#!/usr/bin/env python3
"""More involved type annotations"""


from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) -> Union[T, None]:
    """Given the parameters and the return
    values, add type annotations to the function"""

    if key in dct:
        return dct[key]
    else:
        return default
