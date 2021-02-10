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
    print(moveZeroes([0, 0, 1]))
