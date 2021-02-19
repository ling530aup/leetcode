from typing import List


def dfs(nums, path, used, depth, res):
    if depth == len(nums):
        res.append(path.copy())
        return

    for num in nums:
        if not num in used:
            path.append(num)
            used.add(num)
            dfs(nums, path, used, depth + 1, res)
            path.pop()
            used.remove(num)


def permute(nums: List[int]) -> List[List[int]]:
    if not nums:
        return []
    res = []
    dfs(nums, path=[], used=set(), depth=0, res=res)
    return res


if __name__ == '__main__':
    assert permute([0, 1]) == [[0, 1], [1, 0]]
    assert permute([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
