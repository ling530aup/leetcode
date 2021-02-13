'''

Leetcode-7 整数反转
给你一个 32 位的有符号整数 x ，返回 x 中每位上的数字反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围[2**−31, 2**31− 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''


def reverse(x: int) -> int:
    rt = int(str(abs(x))[::-1])
    if rt > 2 ** 31:
        return 0
    return rt if x > 0 else -rt


if __name__ == '__main__':
    assert reverse(120) == 21
    assert reverse(-123) == 321
    assert reverse(0) == 0
