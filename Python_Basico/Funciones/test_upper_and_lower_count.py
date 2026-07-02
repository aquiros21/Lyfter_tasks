import unittest
from upper_and_lower_count import count_capitals

class CountingSmallWords(unittest.TestCase):

    def test_counting_capitals_small_words(self):
        word = "TeSts"
        result = count_capitals(word)
        self.assertEqual(result, (2, 3))


    def test_counting_capitals_phrases(self):
        word = "This Is a Long Test"
        result = count_capitals(word)
        self.assertEqual(result, (4, 11))

    def test_counting_capitals_empty(self):
        word = ""
        result = count_capitals("")
        self.assertEqual(result, (0,0))



if __name__ == '__main__':
    unittest.main()