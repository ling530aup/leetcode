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
    # assert rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3) == [5, 6, 7, 1, 2, 3, 4]
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    rotate(nums, k)
    print(nums)
    print('---rotate---')
