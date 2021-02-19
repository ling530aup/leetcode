from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    res = [[1]]
    for num in nums:
        _new = res.copy()
        for i_cp in _new:
            i_cp.append(num)
        # print('res = ', res)
        # print('_new = ', _new)
        res = res + _new
    return res


if __name__ == '__main__':
    print(subsets([2, 3]))
