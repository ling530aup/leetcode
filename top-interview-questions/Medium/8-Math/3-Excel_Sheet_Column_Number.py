def titleToNumber(s: str) -> int:
    _map = {chr(ord('A') + i): i + 1 for i in range(26)}
    res = 0
    for index, c in enumerate(s[::-1]):
        res += 26 ** index * _map[c]
    return res


if __name__ == '__main__':
    assert titleToNumber('FXSHRXW') == 2147483647
    assert titleToNumber('AB') == 28
    assert titleToNumber('ZY') == 701
