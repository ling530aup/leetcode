class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        opt = [0] * len(nums)
        opt[0], opt[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            opt[i] = max(opt[i - 1], opt[i - 2] + nums[i])
        return opt[-1]
        
