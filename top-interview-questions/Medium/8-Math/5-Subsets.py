def mySqrt(x: int) -> int:
    left, right = 0, x
    if x <=1:
        return int(x)
    while right - left >= 1e-10:
        mid = (left + right) / 2
        # print(f'left= {left}, right={right}    mid={mid}')
        if mid ** 2 > x:
            right = mid
        elif mid ** 2 < x:
            left = mid
        else:
            return int(mid)

    return int(right)


if __name__ == '__main__':
    assert mySqrt(5) == 2
    assert mySqrt(1) == 1
    assert mySqrt(8) == 2
    assert mySqrt(9) == 3