class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        for left in range(len(nums)):
            if nums[left] == target:
                break

        if left < len(nums) - 1:
            for right in range(len(nums) - 1, -1, -1):
                if nums[right] == target:
                    break
            return [left, right]
        else:
            if nums[left] == target:
                return [left, left]
            else:
                return [-1, -1]

