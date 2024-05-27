#!/usr/bin/env python3
"""Parameterize a unit test"""
from utils import *
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Creates an instance of unittest"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test access nested map method"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
