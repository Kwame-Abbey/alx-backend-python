#!/usr/bin/env python3
"""Test module for GithubOrgClient"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient"""

    @parameterized.expand([
        ("google", {"login": "mock"}),
        ("abc", {"login": "mock"}),
    ])
    @patch('client.get_json', return_value={"login": "mock"})
    def test_org(self, org_name, expected_result, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

        self.assertEqual(result, expected_result)

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
