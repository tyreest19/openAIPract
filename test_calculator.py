"""
Unit tests for the calculator library
"""

from calculator import Calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == Calculator().add(2, 2)

    def test_subtraction(self):
        assert 2 == Calculator().subtract(4, 2)

    def test_divide(self):
        assert 2 == Calculator().divide(4, 2)
