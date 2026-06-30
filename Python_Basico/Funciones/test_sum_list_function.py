import unittest
from sum_list_function import sum_list


class TestSumList (unittest.TestCase):

    def test_sum_list_two_numbers(self):
        numbers = [10, 25]
        result = sum_list(numbers)
        self.assertEqual(result, 35)

    def test_sum_list_negative_numbers(self):
        numbers = [-4, -5, -6]
        result = sum_list(numbers)
        self.assertEqual(result, -15)


    def test_sum_list_using_string(self):
        with self.assertRaises(TypeError):
            sum_list(["only numbers allowed"])


if __name__ == '__main__':
    unittest.main()