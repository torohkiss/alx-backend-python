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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        # Check that the exception message matches the expected key
        self.assertEqual(str(context.exception), str(path[-1]))


if __name__ == "__main__":
    unittest.main()
