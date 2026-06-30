import unittest
from prime_number_function import show_prime

class Testing_prime_numbers(unittest.TestCase):
    
    def test_prime_number_function_few_numbers(self):
        numbers = [7, 8, 13, 15]
        result = show_prime(numbers)
        self.assertEqual(result, [7,13])

    def test_prime_number_function_many_numbers(self):
        numbers = [7, 8, 13, 15, 67, 101, 199, 202, 25]
        result = show_prime(numbers)
        self.assertEqual(result, [7, 13, 67, 101, 199])

    
    def test_prime_number_function_empty_list(self):
        numbers = []
        result = show_prime(numbers)
        self.assertEqual(result,[])
        



if __name__ == '__main__':
    unittest.main()