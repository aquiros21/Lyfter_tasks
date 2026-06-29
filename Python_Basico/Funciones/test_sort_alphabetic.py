import unittest
from sort_alphabetically import sort_alphabetic 

class SortAlphabetically(unittest.TestCase):

    def test_sort_alphabetic_two_words(self):
        words = "berry-apple"
        result = sort_alphabetic(words)
        self.assertEqual(result,("apple-berry"))

    
    def test_sort_alphabetic_many_words(self):
        words = "berry-charlie-apple-dog-elephant"
        result = sort_alphabetic(words)
        self.assertEqual(result,"apple-berry-charlie-dog-elephant")

    
    def test_sort_alphabetic_empty_list(self):
        words = ""
        result = sort_alphabetic("")
        self.assertEqual(result, "")


if __name__ == '__main__':
    unittest.main()