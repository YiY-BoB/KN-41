# test.py
import unittest
from main import sum_even

class TestFunction(unittest.TestCase):
    def test_my_function(self):
        # Тип результату має бути int
        self.assertIsInstance(sum_even([0, 1, 2, 3, 4]), int)
        # Порожній список → 0
        self.assertEqual(sum_even([]), 0)
        # Лише непарні числа → 0
        self.assertEqual(sum_even([1, 3, 5]), 0)
        # Тільки парні числа
        self.assertEqual(sum_even([2, 4, 6]), 12)
        # Змішаний список
        self.assertEqual(sum_even([1, 2, 3, 4, 5, 6]), 12)

if __name__ == '__main__':
    unittest.main()
