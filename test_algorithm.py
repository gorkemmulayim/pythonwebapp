import unittest
from algorithm import isDistinct

class TestContainsSameElement(unittest.TestCase):
    def setUp(self):
        self.multipleElementArrayDistinct = [5, 6, 4, 332, -12, 1, 0]
        self.multipleElementArrayNotDistinct = [10, 55, 4, 20, -6, 1, 4, 3, 3]
        self.emptyArray = []
        self.twoElementArrayDistinct = [1, 2]
        self.twoElementArrayNotDistinct = [1, 1]
        self.oneElementArray = [1]

    def test_successful(self):
        self.assertTrue(isDistinct(self.oneElementArray, 0, 0))

    def test_failed(self):
        self.assertFalse(isDistinct(self.twoElementArrayNotDistinct, 0, 1))

    def test_emptyArray(self):
        self.assertFalse(isDistinct(self.emptyArray, 0, 99))

    def test_oneElementInArray(self):
        self.assertTrue(isDistinct(self.oneElementArray, 0, 0))

    def test_whenIndexesAreSame(self):
        self.assertTrue(isDistinct(self.multipleElementArrayDistinct, 0, 0))

    def test_whenFirstIndexIsNegative(self):
        self.assertFalse(isDistinct(self.multipleElementArrayNotDistinct, -1, 0))

    def test_whenSecondIndexIsNegative(self):
        self.assertFalse(isDistinct(self.multipleElementArrayNotDistinct, 0, -1))

    def test_whenIndexIsOutRange(self):
        self.assertRaises(IndexError, isDistinct, self.multipleElementArrayDistinct, 100, 101)
if __name__ == '__main__':
    unittest.main()

