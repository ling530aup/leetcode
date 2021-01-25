from collections import Counter
from itertools import chain


def intersect(nums1, nums2):
    '''
    借用 python计数器的交集， 计算完成后还原为数组
    '''
    counter = Counter(nums1) & Counter(nums2)
    rt = [counter[key] * [key] for key in counter]
    return list(chain(*rt))


if __name__ == '__main__':
    assert intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]) == [4, 9]
    print('-----intersect-----------')
