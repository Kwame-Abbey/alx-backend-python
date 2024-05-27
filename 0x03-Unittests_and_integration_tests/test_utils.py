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

    @parameterized.expand([
        ({}, ("a",), "KeyError: 'a'"),
        ({"a": 1}, ("a", "b"), "KeyError: 'b"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Raises an exception"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{path[-1]}'")
