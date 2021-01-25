def rotate(nums, k):
    return nums[-k:] + nums[:-k]


if __name__ == '__main__':
    assert rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3) == [5, 6, 7, 1, 2, 3, 4]
    print('---rotate---')
