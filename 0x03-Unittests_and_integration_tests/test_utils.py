#!/usr/bin/env python3
"""
Unit tests for the utils.access_nested_map function.

This module contains parameterized unit tests to verify that
access_nested_map correctly retrieves values from nested mappings.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(unittest.TestCase):
    """
    Test suite for the access_nested_map function.

    This class tests multiple input scenarios using parameterized
    test cases to ensure the function behaves as expected.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
        self, nested_map: Mapping, path: Sequence, expected: Any
    ) -> None:
        """
        Test that access_nested_map returns the expected value
        for a given nested_map and path.

        Parameters
        ----------
        nested_map : Mapping
            The nested dictionary to search.
        path : Sequence
            Tuple of keys representing the path to the target value.
        expected : Any
            The expected value returned by the function.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
