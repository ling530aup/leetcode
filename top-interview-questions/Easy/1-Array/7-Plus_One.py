'''
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/plus-one
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



'''
def plusOne(digits):
    '''
    思路：  类似 数字电路的串行加法器。  用一个flag记录是否有进位，从各位往前面加
    '''
    add_flag = True
    for i in range(len(digits) - 1, -1, -1):
        if add_flag:
            digits[i] += 1

        if digits[i] >= 10:
            add_flag = True
            digits[i] = 0
        else:
            add_flag = False
            break
    if add_flag:
        digits = [1] + digits
    return digits


if __name__ == '__main__':
    assert plusOne([0, 1]) == [0, 2]
    assert plusOne([4,3,2,1]) == [4,3,2,2]
    assert plusOne([0]) == [1]
    assert plusOne([9,9]) == [1,0,0]
    
