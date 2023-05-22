#!/usr/bin/env python3
"""Parameterize a unit test"""
import unittest
from unittest.mock import PropertyMock, patch
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

    def test_public_repos_url(self):
        """mock _public_repos_url"""
        with patch.object(
            GithubOrgClient, 'org', new_callable=PropertyMock
        ) as mock_org:
            # create a default return value
            mock_org.return_value = {
                'repos_url': 'abc.github.go/emiwest007/how-to-kill-anyone'
            }
            test_org = GithubOrgClient('emiwest')  # dummy org_name
            test_repo_url = test_org._public_repos_url
            self.assertEqual(
                test_repo_url, mock_org.return_value.get('repos_url'))
            mock_org.assert_called_once()

    @patch('client.get_json', return_value=[{'name': 'ALX'},
                                            {'name': 'Emmanuel'},
                                            {'name': 'De-light'}])
    def test_public_repos(self, mock_get_json):
        """Implementations to unit-test GithubOrgClient.public_repos"""
        repo_list = ['truth', 'ruby-openid-apps-discovery', 'autoparse']
        with patch.object(
            GithubOrgClient, '_public_repos_url',
                new_callable=PropertyMock, return_value={'repos': repo_list}
        ) as mock_pub:
            tester = GithubOrgClient("emiwest")
            tester_repo = tester.public_repos()
            mock_pub.assert_called_once()
            mock_get_json.assert_called_once()
            for idx in range(3):
                print(mock_get_json.return_value[idx]['name'])
                self.assertIn(
                    mock_get_json.return_value[idx]['name'], tester_repo)


if __name__ == "__main__":
    unittest.main()
