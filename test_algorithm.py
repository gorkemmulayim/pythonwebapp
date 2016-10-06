import unittest
from algorithm import isDistinct

class TestContainsSameElement(unittest.TestCase):
    def setUp(self):
        self.array = [10, 55, 4, 20, -6, 1, 4, 3, 3]

    def test_successful(self):
        self.assertTrue(isDistinct(self.array, 7, 8))

    def test_failed(self):
        self.assertFalse(isDistinct(self.array, 0, 8))

    def test_emptyArray(self):
        self.assertFalse(isDistinct([], 0, 99))

    def test_whenIndexesAreSame(self):
        self.assertTrue(isDistinct(self.array, 0, 0))

    def test_whenFirstIndexIsNegative(self):
        self.assertFalse(isDistinct(self.array, -1, 0))

    def test_whenSecondIndexIsNegative(self):
        self.assertFalse(isDistinct(self.array, 0, -1))
    def test_whenIndexIsOutRange(self):
        self.assertRaises(IndexError, isDistinct, self.array, 100, 101)
if __name__ == '__main__':
    unittest.main()

