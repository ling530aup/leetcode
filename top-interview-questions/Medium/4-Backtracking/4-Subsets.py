from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    res = [[]]
    for i in nums:
        res = res + [[i] + num for num in res]
    return res


if __name__ == "__main__":
    assert subsets([1, 2, 3]) == [[], [1], [2], [2, 1], [3], [3, 1], [3, 2], [3, 2, 1]]
    assert subsets([]) == [[]]
    assert subsets([0]) == [[], [0]]
