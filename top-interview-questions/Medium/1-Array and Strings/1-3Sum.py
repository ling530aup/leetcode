class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()

        for i, v in enumerate(nums[:-2]):
            if i >= 1 and nums[i - 1] == v:
                continue
            _dict = dict()
            for x in nums[i + 1:]:

                if x not in _dict:
                    _dict[-v - x] = 1
                else:
                    res.add((v, x, -x - v))

        return map(list, res)
