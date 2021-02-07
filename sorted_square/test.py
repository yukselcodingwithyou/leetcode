import unittest
from solution import Solution

class TestSortedSquares(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_sorted_squares(self):
        self.assertListEqual(self.solution.sorted_squares([-7,-3,2,3,11]), [4,9,9,49,121], "Should be [4,9,9,49,121]")

if __name__ == '__main__':
    unittest.main()