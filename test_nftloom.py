# test_nftloom.py
"""
Tests for NftLoom module.
"""

import unittest
from nftloom import NftLoom

class TestNftLoom(unittest.TestCase):
    """Test cases for NftLoom class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = NftLoom()
        self.assertIsInstance(instance, NftLoom)

    def test_run_method(self):
        """Test the run method."""
        instance = NftLoom()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
