#!/usr/bin/env python3
"""Parameterize a unit test"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test that GithubOrgClient.org returns the correct value"""

    @parameterized.expand([
        ("google", {'name': 'google'}),
        ("abc", {"name": 'abc'}),
    ])
    @patch('client.get_json')
    def test_org(self, org, result, mock_get_json):
        """test org method while mocking get_json"""
        mock_get_json.return_value = result
        tester = GithubOrgClient(org)
        response = tester.org
        self.assertEqual(response, result)
        mock_get_json.assert_called_once()


if __name__ == "__main__":
    unittest.main()
