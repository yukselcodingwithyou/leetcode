import unittest
from solution import Solution



class TestMaxConsecutiveOnes(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_should_be_5(self):
        self.assertEqual(self.solution.find_max_consecutive_ones([1, 1, 1, 0, 1,1,1,1,1]), 5, "Should be 5")

    def test_should_be_1(self):
        self.assertEqual(self.solution.find_max_consecutive_ones([1]), 1, "Should be 1")

    def test_should_be_0(self):
        self.assertEqual(self.solution.find_max_consecutive_ones([0]), 0, "Should be 0")

if __name__ == '__main__':
    unittest.main()