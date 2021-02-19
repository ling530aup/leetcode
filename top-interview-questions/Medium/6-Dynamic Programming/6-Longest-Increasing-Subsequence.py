from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                dp[j] = max(dp[j], dp[i] + 1)
    # print(dp)
    return max(dp)


if __name__ == '__main__':
    assert lengthOfLIS([1]) == 1
    assert lengthOfLIS([1, 2]) == 2
    assert lengthOfLIS([2, 1]) == 1
    assert lengthOfLIS([1, 1]) == 1
    assert lengthOfLIS([1, 0, 2, 1, 4, 0]) == 3
    assert lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6
