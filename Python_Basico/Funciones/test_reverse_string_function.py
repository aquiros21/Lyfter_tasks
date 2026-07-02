import unittest
from reverse_string_function import reverse_string

class TestReverseString(unittest.TestCase):

    def test_reverse_string_small_word(self):
        word = "test"
        result = reverse_string(word)
        self.assertEqual(result, "tset")


    def test_reverse_string_phrase(self):
        phrase = "This is a full test"
        result = reverse_string(phrase)
        self.assertEqual(result, "tset lluf a si sihT")


    def test_reverse_string_empty_string(self):
        result = reverse_string("")
        self.assertEqual(result, "")


if __name__ == '__main__':
    unittest.main()