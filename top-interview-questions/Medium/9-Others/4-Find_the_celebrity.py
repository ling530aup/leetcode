# Find_the_celebrity

def knows(a, b, m):
    return m[a][b] == 1


def findCelebrity(m: int) -> int:
    n = len(m)
    _set = set(range(n))

    if n < 2:
        return -1
    while len(_set) > 1:
        a, b = tuple(list(_set)[:2])
        if knows(a, b, m):
            _set.remove(a)
        else:
            _set.remove(b)
    # ------------final check-----------------------
    ls = list(_set)
    for i in range(len(ls)):
        for j in range(n):
            if ls[i] != j and (knows(ls[i], j, m) or (not knows(j, ls[i], m))):
                if ls[i] in _set:
                    _set.remove(ls[i])
                break
    if _set:
        return list(_set)[0]
    else:
        return -1


if __name__ == '__main__':
    assert findCelebrity([[1, 0, 1], [1, 1, 0], [0, 1, 1]]) == -1
    assert findCelebrity([[1, 1, 0], [0, 1, 0], [1, 1, 1]]) == 1
