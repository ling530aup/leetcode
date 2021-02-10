def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1
    neg_flag = (n < 0)
    result = x
    # for i in range(abs(n)):
    i = abs(n)
    while i > 1:
        result *= result
        result *= (x ** (i % 2))
        print("result = ", result)
        i = int(i / 2)
    if neg_flag:
        return 1 / result
    else:
        return result


if __name__ == '__main__':
    x = 8.84372
    n = -5

    print(myPow(x, n))
