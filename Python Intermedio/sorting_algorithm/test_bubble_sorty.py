import unittest
import random
from bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):

    def test_bubble_sort_small_list(self):
        sorting_list = [10, 5, 20, 6, 9]
        bubble_sort(sorting_list)
        self.assertEqual(sorting_list, [5, 6, 9, 10, 20])


    def test_bubble_sort_large_list(self):
        import random
        sorting_list = random.sample(range(1000), 100)
        expected = sorted(sorting_list)
        bubble_sort(sorting_list)
        self.assertEqual(sorting_list, expected)


    def test_bubble_sort_empty_list(self):
        sorting_list = []
        bubble_sort(sorting_list)
        self.assertEqual(sorting_list, [])   


    def test_bubble_sort_invalid_input(self):
        with self.assertRaises(TypeError):
            bubble_sort("not a list")


if __name__ == '__main__':
    unittest.main()