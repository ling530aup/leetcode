from typing import List


def evalRPN(tokens: List[str]) -> int:
    sk = []
    for s in tokens:
        if not s in ['-', '+', '/', '*']:
            sk.append(s)
        else:
            a = sk.pop()
            b = sk.pop()
            sk.append(eval(f'{b} {s} {a}'))
    return sk[0]


if __name__ == '__main__':
    assert evalRPN(["2", "1", "+", "3", "*"]) == 9