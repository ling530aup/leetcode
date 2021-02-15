'''
LeetCode 189. 旋转数组[中等难度]

给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

进阶：

尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
def rotate_right(nums):
    tail = nums[len(nums) - 1]
    for i in range(len(nums) - 2, -1, -1):
        nums[i + 1] = nums[i]
    nums[0] = tail


def rotate(nums, k):
    '''
        用多次循环右移解决。 时间上市超时的。
        正确思路，  一定存在一个有向图， 使得按秩序交换后，得到目标数组。  时间O(n) 空间O(1)
    '''
    for i in range(k):
        rotate_right(nums)


if __name__ == '__main__':
    assert rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3) == [5, 6, 7, 1, 2, 3, 4]
    assert rotate(nums=[-1,-100,3,99], k=2) == [3,99,-1,-100]
    
