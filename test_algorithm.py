import unittest
from algorithm import containsSameElement

class TestContainsSameElement(unittest.TestCase):
  def setUp(self):
    self.array = [10, 55, 4, 20, -6, 1, 4, 3, 3]

  def test_successful(self):
    self.assertTrue(containsSameElement(self.array, len(self.array) - 2, len(self.array) - 1))

  def test_failed(self):
    self.assertFalse(containsSameElement(self.array, 0, 1))

  def test_emptyArray(self):
    self.assertFalse(containsSameElement([], 0, 99))

  def test_whenIndexIsOutOfRange(self):
    self.assertRaises(IndexError, containsSameElement(self.array, 0, 0))

  def test_whenIndexesAreSame(self):
    self.assertFalse(containsSameElement(self.array, 0, 0))

  def test_whenArrayIsNone(self):
    self.assertRaises(TypeError, containsSameElement(None, 0, 99))

  def test_whenIndexIsNegative(self):
    self.assertTrue(containsSameElement(self.array, -1, 0))

  def test_searchingNoneFailed(self):
    self.assertFailed(containsSameElement([None], 0, (self.array) - 1))
 

if __name__ == '__main__':
    unittest.main()
