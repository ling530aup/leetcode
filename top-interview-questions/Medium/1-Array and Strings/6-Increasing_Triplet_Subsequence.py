class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        small, mid = float('inf'), float('inf')
        for i in nums:
            if small > i:
                small = i
            else:
                if small < i < mid:
                    mid = i
            if small < mid < i: 
                return True

        return False
      
