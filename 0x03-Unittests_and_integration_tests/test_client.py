#!/usr/bin/env python3
"""Test module for GithubOrgClient"""
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient"""

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url',
           new_callable=unittest.mock.PropertyMock)
    def test_public_repos(self, mock_repos_url, mock_get_json):
        """Test public_repos method"""

        # Define mocked data
        mock_repos_url.return_value = (
            "https://api.github.com/orgs/test-org/"
            "repos"
        )

        mock_get_json.return_value = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache"}},
            {"name": "repo3", "license": {"key": "mit"}},
        ]

        client = GithubOrgClient("test-org")

        repos = client.public_repos(license="mit")

        mock_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/test-org/repos")

        self.assertEqual(repos, ["repo1", "repo3"])

    def test_public_repos_url(self):
        """Test that _public_repos_url returns the correct
        value based on the mocked org payload
        """
        expected_repos_url = "https://api.github.com/orgs/test-org/repos"
        mock_org_payload = {"repos_url": expected_repos_url}

        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as mock_org:
            mock_org.return_value = mock_org_payload
            client = GithubOrgClient("test-org")
            result = client._public_repos_url

            self.assertEqual(result, expected_repos_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """Test has_license method"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected_result)


@parameterized_class([
    {
        "org_payload": TEST_PAYLOAD[0][0],
        "repos_payload": TEST_PAYLOAD[0][1],
        "expected_repos": TEST_PAYLOAD[0][2],
        "apache2_repos": TEST_PAYLOAD[0][3]
    }
])
class testIntegrationGithubOrgClient(unittest.TestCase):
    """ testIntegrationGithubOrgClient class"""

    @classmethod
    def setUpClass(cls):
        """ Start patching requests.get """
        test_payload = {
            "https://api.github.com/orgs/google": cls.org_payload,
            "https://api.github.com/orgs/google/repos": cls.repos_payload,
        }

        def side_effect(url: str):
            """ Set the side effect of the mock """
            if url in test_payload:
                mock = Mock()
                mock.json.return_value = test_payload[url]
                return mock
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=side_effect)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down class"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ Test public repo"""
        org = GithubOrgClient("google")
        self.assertEqual(org.public_repos(), self.expected_repos)
