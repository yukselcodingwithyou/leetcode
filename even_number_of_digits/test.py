import unittest
from solution import Solution




class TestMaxConsecutiveOnes(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_should_be_1(self):
        self.assertEqual(self.solution.find_even_number_of_digits([555,901,482,1771]), 1, "Should be 1")

    def test_should_be_2(self):
        self.assertEqual(self.solution.find_even_number_of_digits([12,345,2,6,7896]), 2, "Should be 2")

    def test_should_be_0(self):
        self.assertEqual(self.solution.find_even_number_of_digits([1]), 0, "Should be 0")

if __name__ == '__main__':
    unittest.main()