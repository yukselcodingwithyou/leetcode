

class Solution:

    """
    Returns sorted list of squares of numbers in array
    """
    def sorted_squares(self, nums):
        return sorted(list(map(lambda num : abs(num) * abs(num), nums)))
        # l = list(map(lambda num : abs(num) * abs(num), nums))
        # l.sort()
        # return l
