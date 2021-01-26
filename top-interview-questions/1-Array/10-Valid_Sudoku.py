import numpy as np

board = \
    [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


# board = \
#          [["8", "3", ".", ".", "7", ".", ".", ".", "."]
#         , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
#         , [".", "9", "8", ".", ".", ".", ".", "6", "."]
#         , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
#         , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
#         , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
#         , [".", "6", ".", ".", ".", ".", "2", "8", "."]
#         , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
#         , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


def remove_dot(arr):
    ls = []
    for i in arr:
        if i != '.':
            ls.append(i)
    ls.append('.')
    return ls


def isValidSudoku(board):
    # check all item is in 1-9 and '.'
    sset = set(['1', '2', '3', '4', '5', '6', '7', '8', '9', '.'])
    for i in range(9):
        for j in range(9):
            if board[i][j] not in sset:
                print("not in sset")
                return False
    # ---------检查 列和行 合法--------------
    board = np.array(board)
    for i in range(9):
        if len(remove_dot(board[:, i])) != len(set(board[:, i])):
            return False
        if len(remove_dot(board[i, :])) != len(set(board[i, :])):
            print(f'{i} row error')
            return False
    # ---------检查 九宫格合法--------------
    # remove_dot(board[0:2, i])
    for x in [0, 3, 6]:
        for y in [0, 3, 6]:
            if len(remove_dot(board[x:x + 3, y:y + 3].flatten())) != len(set(board[x:x + 3, y:y + 3].flatten())):
                return False

    return True


if __name__ == '__main__':
    assert isValidSudoku(board) == True
    print('--------test isValidSudoku ------')
