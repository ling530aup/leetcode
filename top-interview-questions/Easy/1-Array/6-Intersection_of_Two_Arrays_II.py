'''
Leetcode 350. 两个数组的交集 II （难度：简单）
给定两个数组，编写一个函数来计算它们的交集。


'''
from collections import Counter
from itertools import chain


def intersect(nums1, nums2):
    '''
    借用 python计数器的交集， 计算完成后还原为数组
    '''
    counter = Counter(nums1) & Counter(nums2)
    rt = [counter[key] * [key] for key in counter]
    return list(chain(*rt))

'''
另外一种思路：
两个数组分别排序。 用i,j 分别为两数组指针，并且从左向右移动
while i,j 不超出最大index
    if num1[i] == num2[j] -》保存该值
    if num1[i] < num2[j] -> i++
    if num1[i] > num2[j] -> j++
    
重复使用 num1 保存结果，有利于节省空间。 最后时间复杂度为两个排序 O(mlogm+nlogn)空间复杂度O(1)
'''


if __name__ == '__main__':
    assert intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]) == [4, 9]
    assert intersect(nums1=[1,2,2,1], nums2=[2,2]) == [2,2]
  
