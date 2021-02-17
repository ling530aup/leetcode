'''
LeetCode 283. 移动零(简单)
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
'''


def moveZeroes(nums):
    '''
    冒泡排序的一个变种。 i是当前挤出0后摆放的位置。   内循环j和冒泡内循环一样，像上冒泡，挤出0
    '''
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] != 0:
            continue
        for j in range(i, len(nums) - 1):
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


if __name__ == '__main__':
    assert moveZeroes([0, 0, 1]) == [1, 0, 0]
    assert moveZeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
