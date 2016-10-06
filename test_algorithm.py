import unittest
from algorithm import containsSameElement

class TestContainsSameElement(unittest.TestCase):
    def setUp(self):
        self.array = [10, 55, 4, 20, -6, 1, 4, 3, 3]

    def test_successful(self):
        self.assertTrue(containsSameElement(self.array, 0, len(self.array) - 1))

    def test_failed(self):
        self.assertFalse(containsSameElement(self.array, 0, 1))

    def test_emptyArray(self):
        self.assertFalse(containsSameElement([], 0, 99))

    def test_whenIndexesAreSame(self):
        self.assertFalse(containsSameElement(self.array, 0, 0))

    def test_whenIndexIsNegative(self):
        self.assertTrue(containsSameElement(self.array, -1, 0))


if __name__ == '__main__':
    unittest.main()

