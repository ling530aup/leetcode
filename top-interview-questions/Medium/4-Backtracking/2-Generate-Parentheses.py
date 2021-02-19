from typing import List


def dfs(n, path, _open, close, res):
    if _open > n or close > n or _open < close:
        return

    if len(path) == n * 2:
        res.append(path)
        return

    dfs(n, path + '(', _open + 1, close, res)
    dfs(n, path + ')', _open, close + 1, res)


def generateParenthesis(n: int) -> List[str]:
    res = []
    if n <= 0:
        return res
    dfs(n, "", 0, 0, res)
    return res


if __name__ == '__main__':
    assert set(generateParenthesis(3)) == set(["((()))", "(()())", "(())()", "()(())", "()()()"])
    assert set(generateParenthesis(1)) == set(["()"])
