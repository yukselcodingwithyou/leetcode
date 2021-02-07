import math

class Solution:

    '''
    Finds number of even digit of numbers in an array.
    '''
    def find_even_number_of_digits(self, nums):
       return len(list(filter(lambda x :x % 2 == 0, list(map(lambda num : (int(math.log10(num)) + 1), nums)))))