import unittest
from difference_of_squares import (square_of_sum, sum_of_squares, difference_of_squares)

class RtDifferenceOfSquares(unittest.TestCase):
    def test_square_of_sum_3(self):
        self.assertEqual(square_of_sum(3), (1 + 2 + 3) ** 2)
    def test_square_of_sum_1(self):
        self.assertEqual(square_of_sum(1), 1)
    def test_square_of_sum_4(self):
        self.assertEqual(square_of_sum(4), (1 + 2 + 3 + 4) ** 2)
    def test_sum_of_squares_1(self):
        self.assertEqual(sum_of_squares(1), 1)
    def test_sum_of_squares_3(self):
        self.assertEqual(sum_of_squares(3), 1 ** 2 + 2 ** 2 + 3 ** 2)
    def test_sum_of_squares_4(self):
        self.assertEqual(sum_of_squares(4), 1 ** 2 + 2 ** 2 + 3 ** 2 + 4 ** 2)
    def test_difference_of_squares_1(self):
        self.assertEqual(difference_of_squares(1), 0)
    def test_difference_of_squares_2(self):
        self.assertEqual(difference_of_squares(2), 9 - 5)
    def test_difference_of_squares_3(self):
        self.assertEqual(difference_of_squares(3), 36 - 14)
