def trailingZeroes(n: int) -> int:
    c = 0
    while n >= 5:
        n = int(n / 5)
        c += n
    return c


if __name__ == '__main__':
    pass
