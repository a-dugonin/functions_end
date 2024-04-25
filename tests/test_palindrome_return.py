import unittest

from task_3.palindrome_return import can_be_poly


class TestCanBePoly(unittest.TestCase):
    def test_can_be_poly(self) -> None:
        self.assertEqual(can_be_poly('abcba'), True)
        self.assertEqual(can_be_poly('abbbc'), False)
        self.assertEqual(can_be_poly(5), "В функцию передан не строковый аргумент")


if __name__ == '__main__':
    unittest.main()
