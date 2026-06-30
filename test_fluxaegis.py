# test_fluxaegis.py
"""
Tests for FluxAegis module.
"""

import unittest
from fluxaegis import FluxAegis

class TestFluxAegis(unittest.TestCase):
    """Test cases for FluxAegis class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FluxAegis()
        self.assertIsInstance(instance, FluxAegis)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FluxAegis()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
