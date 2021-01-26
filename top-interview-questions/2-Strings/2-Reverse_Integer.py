def reverse(x: int) -> int:
    rt = int(str(abs(x))[::-1])
    if rt > 2 ** 31:
        return 0
    return rt if x > 0 else -rt


if __name__ == '__main__':
    assert reverse(x=120) == 21
    print('---reverse---')
