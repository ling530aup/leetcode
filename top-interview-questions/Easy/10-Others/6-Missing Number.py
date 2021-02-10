class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        rt = set(range(len(nums)+1)) - set(nums)
        return list(rt)[0]
        
        
        
