#!/usr/bin/env python3
"""Test module for GithubOrgClient"""
import unittest
from unittest.mock import patch, PropertyMock
# from parameterized import parameterized
from client import GithubOrgClient


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
