#!/usr/bin/env python3
"""Parameterize a unit test"""
import unittest
from unittest.mock import MagicMock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """Test the access nested map function from utils module"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, ret_value):
        """Test the access nested map function from utils module"""
        self.assertEqual(access_nested_map(nested_map, path), ret_value)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test the access nested map function raised errors"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """test the get json function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("utils.requests")
    def test_get_json(self, test_url, test_payload, mock_requests):
        """test the get json function"""
        # print(f"Here======>\n{test_payload}")
        # bcos request.get returns a Response object,
        # I need to mock a response object
        mock_response = MagicMock()
        # then imitate .json() method and  pass in my payload as return value
        mock_response.json.return_value = test_payload
        mock_requests.get.return_value = mock_response

        self.assertEqual(get_json(test_url), test_payload)


if __name__ == "__main__":
    unittest.main()
