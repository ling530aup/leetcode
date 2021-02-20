from typing import List

def findPeakElement(nums: List[int]) -> int:
    if len(nums) < 3:
        nums.index(max(nums))

    for i in range(1, len(nums) - 1):
        if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
            return i
    return nums.index(max(nums))


if __name__ == '__main__':
    assert findPeakElement([1]) == 0
    assert findPeakElement([1, 2]) == 1
    assert findPeakElement([2, 1]) == 0
    assert findPeakElement([3, 1, 2]) == 0
    assert findPeakElement([3, 2, 1]) == 0
    assert findPeakElement([1, 3, 2]) == 1
