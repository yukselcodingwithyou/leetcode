
class Solution:

    def find_max_consecutive_ones(self, nums):
        consecutive_ones = 0
        ones = 0
        for num in nums:
            if num == 1:
                ones += 1
            else:
                consecutive_ones = max(consecutive_ones, ones)
                ones = 0
        return max(consecutive_ones, ones)



