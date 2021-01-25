def removeDuplicates(nums):
    ''' 遍历数组， 如果和邮编相等，删除当前元素。否则继续向前搜索'''
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            nums.remove(nums[i])
        else:
            i += 1
    return len(nums)


if __name__ == '__main__':
    assert removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
    print('---removeDuplicates---')
