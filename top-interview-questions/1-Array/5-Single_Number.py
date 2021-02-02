from collections import Counter

#方法1 懒人做法，调用Counter
def singleNumber(nums):
    count = Counter(nums)
    for key in count:
        if count[key] == 1:
            return key
    return -1

#方法2
# 一个集合记录是否访问过元素
def singleNumber2(nums):
        _set = set()
        for item in nums:
            if item in _set:
                _set.remove(item)
            else:
                _set.add(item)
        return list(_set)[0]
    
if __name__ == '__main__':
    assert singleNumber([4, 1, 2, 1, 2]) == 4
    print('----------------')
