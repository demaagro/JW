# test_jwtauth.py
"""
Tests for JWTAuth module.
"""

import unittest
from jwtauth import JWTAuth

class TestJWTAuth(unittest.TestCase):
    """Test cases for JWTAuth class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = JWTAuth()
        self.assertIsInstance(instance, JWTAuth)
        
    def test_run_method(self):
        """Test the run method."""
        instance = JWTAuth()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
