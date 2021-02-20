from typing import List


def find_head(board, str):
    res = []
    n_row, n_col = len(board), len(board[0])
    for row in range(board):
        for col in range(n_col):
            if str[0] == exist[row][col]:
                res.append((row, col))
    return res


def dfs(board, visited, word, n_row, n_col):
    pass


def exist(board: List[List[str]], word: str) -> bool:
    # n_row, n_col = len(board), len(board[0])
    # ls = find_head(board, str)
    # for
    # visited = set([(n_row, n_col)])
    # for
    pass

if __name__ == '__main__':
    assert exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], 'ABCCED')
    assert exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], 'SEE')
    assert not exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], 'ABCB')
