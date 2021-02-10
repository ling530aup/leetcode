import numpy as np

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = -int(1e10)
        for index, item in enumerate(nums):
            max_sum = max(max_sum, item+curr_sum)
            curr_sum = max(0, item, item+curr_sum)
        return max_sum
        
    
