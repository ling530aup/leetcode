import random
import copy
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        ls = copy.copy(self.nums)
        for i in range(len(ls)):
            swap_i = random.randrange(i, len(ls))
            ls[i], ls[swap_i] = ls[swap_i], ls[i]
        return ls


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
