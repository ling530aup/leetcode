from collections import Counter


def twoSum(nums, target):
    '''
        用集合记录 target - item。  一个难处理的点：  有可能两个元素相等。
        待优化。偷懒用了Counter 判断有几个target/2 存在
    '''
    ls = set(nums)
    for index, item in enumerate(nums):
        if target - item in ls:
            if target != (target - item) * 2:
                return [index, nums.index(target - item)]
            else:
                if Counter(nums)[item] == 2:
                    return [index, nums.index(target - item, index + 1)]
                else:
                    continue


if __name__ == '__main__':
    print(twoSum(nums=[3, 3], target=6))
