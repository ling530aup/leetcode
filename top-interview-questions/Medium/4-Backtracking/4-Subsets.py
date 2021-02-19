from typing import List


def dfs(nums, visited, res):
    if not (nums - set(visited)):
        return
    for num in nums - set(visited):
        visited.append(num)
        # print('visited = ', visited)
        res.add(str(sorted(visited)))
        dfs(nums, visited, res)
        visited.pop()

        # print('res = ', res)


def subsets(nums: List[int]) -> List[List[int]]:
    res = {str([])}
    if not nums:
        return res
    dfs(set(nums), visited=[], res=res)
    return list(map(eval, res))


if __name__ == '__main__':
    print(subsets([1, 2, 3, 4, 5, 6, 7, 8, 9]))
