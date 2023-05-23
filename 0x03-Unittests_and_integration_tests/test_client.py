#!/usr/bin/env python3
"""Parameterize a unit test"""
import unittest
from unittest.mock import PropertyMock, patch
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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
                                            {'name': 'OK'}])
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
                # print(mock_get_json.return_value[idx]['name'])
                self.assertIn(
                    mock_get_json.return_value[idx]['name'], tester_repo)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test GithubOrgClient's has_license method
        Args:
            repo (dict): dictionary
            license_key (str): license in the repo dict
        """
        test_instance = GithubOrgClient('holberton')
        license_available = test_instance.has_license(repo, license_key)
        self.assertEqual(license_available, expected)


def requests_get(*args, **kwargs):
    """
    Function that mocks requests.get function
    Returns the correct json data based on the given input url
    """
    class MockResponse:
        """
        Mock response
        """

        def __init__(self, json_data):
            self.json_data = json_data

        def json(self):
            return self.json_data

    if args[0] == "https://api.github.com/orgs/google":
        return MockResponse(TEST_PAYLOAD[0][0])
    if args[0] == TEST_PAYLOAD[0][0]["repos_url"]:
        return MockResponse(TEST_PAYLOAD[0][1])


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    [(TEST_PAYLOAD[0][0], TEST_PAYLOAD[0][1], TEST_PAYLOAD[0][2],
      TEST_PAYLOAD[0][3])]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test for the GithubOrgClient.public_repos method
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up function for TestIntegrationGithubOrgClient class
        Sets up a patcher to be used in the class methods
        """
        cls.get_patcher = patch('utils.requests.get', side_effect=requests_get)
        cls.get_patcher.start()
        cls.client = GithubOrgClient('google')

    @classmethod
    def tearDownClass(cls):
        """
        Tear down resources set up for class tests.
        Stops the patcher that had been started
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test public_repos method without license
        """
        self.assertEqual(self.client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test public_repos method with license
        """
        self.assertEqual(
            self.client.public_repos(license="apache-2.0"),
            self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
