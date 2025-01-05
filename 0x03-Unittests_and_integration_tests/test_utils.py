#!/usr/bin/env python3
"""Parameterize a unit test"""


from utils import access_nested_map
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Testing access_nested_map using parameterized"""

    @parameterized.expand([
        ({"a": 1}, ("a",)),
        ({"a": {"b": 2}}, ("a",)),
        ({"a": {"b": 2}}, ("a", "b")),
        ])
    def test_access_nested_map(self, nested_map, path):
        self.assertEqual(access_nested_map(nested_map, path), nested_map['a']
                         if len(path) == 1 else nested_map['a']['b'])


if __name__ == "__main__":
    unittest.main()
