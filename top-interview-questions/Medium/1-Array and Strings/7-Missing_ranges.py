from typing import List


def transf(t):
    if t[0] == t[1]: return str(t[0])
    return f'{t[0]}->{t[1]}'


def findMissingRanges(nums: List[int], lower: int, upper: int) -> List[str]:
    nums = [lower - 1] + nums + [upper + 1]
    ans = []
    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] > 1:
            ans.append((nums[i - 1] + 1, nums[i] - 1))

    return list(map(transf, ans))


if __name__ == '__main__':
    assert findMissingRanges([0, 1, 3, 50, 75], 0, 99) == ["2", "4->49", "51->74", "76->99"]
