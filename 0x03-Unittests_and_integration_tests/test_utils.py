#!/usr/bin/env python3
"""Parameterize a unit test"""


from utils import access_nested_map
import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union
from unittest.mock import patch


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
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: str) -> None:
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(error.exception.args[0], expected)


class TestGetJson(unittest.TestCase):
    """Tests the get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        with patch('requests.get', return_value=mock_response) as mock_get:
            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)


if __name__ == "__main__":
    unittest.main()
