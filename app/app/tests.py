"""
Sample tests
"""

from django.test import SimpleTestCase
from . import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """test calc together"""
        res = calc.add(5, 7)

        self.assertEqual(res, 12)

    def test_subtract_numbers(self):
        """Test subtracting numbers"""
        res = calc.subtract(32, 11)

        self.assertEqual(res, 21)
