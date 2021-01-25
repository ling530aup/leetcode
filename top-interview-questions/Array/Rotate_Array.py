def rotate(nums, k):
    #return nums[-k:] + nums[:-k]

    for i in range(k):
        tail = nums[-1]
        for j in range(len(nums) - 1):
            nums[i+1] = nums[i]
        nums[0] = tail
        print(f't = {tail}')
    return nums

if __name__ == '__main__':
    # assert rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3)
    # print('------')
    print(rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3))
