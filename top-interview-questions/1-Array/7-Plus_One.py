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
    print('-----plusOne-----------')
