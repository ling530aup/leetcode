from collections import Counter


def singleNumber(nums):
    count = Counter(nums)
    for key in count:
        if count[key] == 1:
            return key
    return -1


if __name__ == '__main__':
    assert singleNumber([4, 1, 2, 1, 2]) == 4
    print('----------------')
