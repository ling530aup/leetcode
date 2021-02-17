from typing import List


def canJump(nums: List[int]) -> bool:
    jump = [index + item for index, item in enumerate(nums)]
    max_j = nums[0]
    while max_j != max(jump[:max_j + 1]) and max_j < len(nums) - 1:
        max_j = max(jump[:max_j + 1])
    return max_j >= len(nums) - 1


if __name__ == '__main__':
    assert canJump([2, 3, 1, 1, 4]) == True
    assert canJump([3, 2, 1, 0, 4]) == False
