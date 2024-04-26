import unittest

from task_4.unique_cipher import count_unique_characters, message


class TestUniqueCipher(unittest.TestCase):
    def test_unique_cipher(self):
        self.assertEqual(count_unique_characters(message), 5)
        self.assertRaises(ValueError, count_unique_characters, 5)


if __name__ == '__main__':
    unittest.main()
