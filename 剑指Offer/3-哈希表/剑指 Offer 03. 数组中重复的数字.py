class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        visited = set()
        for num in nums:
            if num in visited:
                return num
            else:
                visited.add(num)