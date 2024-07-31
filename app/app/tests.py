from django.test import SimpleTestCase
from app import calc 

class TestCalc(SimpleTestCase):
    def test_add_numbers(self  ):
        self.assertEqual(calc.add(3, 8), 11)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)