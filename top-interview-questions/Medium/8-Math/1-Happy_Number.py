def isHappy(n: int) -> bool:
    _set = set([n])
    while n:
        n = sum([int(i) ** 2 for i in str(n)])
        if n==1:
            return True
        if n in _set:
            return False
        _set.add(n)
    return True


if __name__ == '__main__':
    assert isHappy(19)
    assert isHappy(1)
    assert not isHappy(2)
