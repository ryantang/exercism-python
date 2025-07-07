import unittest

from list_ops import (
    append, 
    concat,
    filter as list_ops_filter,
    length, 
    map as list_ops_map,
    foldl,
    foldr,
    reverse
)

class RtListOpsTest(unittest.TestCase):
    def test_append(self):
        self.assertEqual(append([1,2,3],['a','b','c']), [1,2,3,'a','b','c'])
    def test_concat(self):
        self.assertEqual(concat([[1,2,3],['a','b','c'],[4,5,6]]), [1,2,3,'a','b','c',4,5,6])
    def test_filter(self):
        self.assertEqual(list_ops_filter(lambda x: x % 2 == 1, [1, 2, 3, 5]), [1, 3, 5])
    def test_length_zero(self):
        self.assertEqual(length([]), 0)
    def test_length_nonzero(self):
        self.assertEqual(length([1, 2, 3]), 3)
    def test_map_non_empty_list(self):
        self.assertEqual(list_ops_map(lambda x: x + 1, [1, 3, 5, 7]), [2, 4, 6, 8])
    def test_foldl_direction_independent_function_applied_to_non_empty_list(self):
        self.assertEqual(foldl(lambda acc, el: el + acc, [1, 2, 3, 4], 5), 15)
    def test_foldl_direction_dependent_function_applied_to_non_empty_list(self):
        self.assertEqual(foldl(lambda acc, el: el / acc, [1, 2, 3, 4], 24), 64)
    def test_reverse(self):
        self.assertEqual(reverse([1, 2, 3, 4]), [4,3,2,1])
    def test_foldr_direction_independent_function_applied_to_non_empty_list(self):
        self.assertEqual(foldr(lambda acc, el: el + acc, [1, 2, 3, 4], 5), 15)
    def test_foldr_direction_dependent_function_applied_to_non_empty_list(self):
        self.assertEqual(foldr(lambda acc, el: el / acc, [1, 2, 3, 4], 24), 9)
