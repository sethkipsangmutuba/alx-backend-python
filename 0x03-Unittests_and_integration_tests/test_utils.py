#!/usr/bin/env python3
"""Unit tests for utils.py"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",)),
        ({"a": {"b": 2}}, ("a",)),
        ({"a": {"b": 2}}, ("a", "b"))
    ])
    def test_access_nested_map(self, nested_map, path):
        """Test that access_nested_map returns expected result."""
        self.assertEqual(access_nested_map(nested_map, path), path[-1] if len(path) == 1 else nested_map[path[0]][path[-1]] if len(path) == 2 else 1)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that KeyError is raised for invalid path."""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
