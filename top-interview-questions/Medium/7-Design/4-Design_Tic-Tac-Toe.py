import numpy as np


class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.m = np.full((n, n), -1)
        self.n = n

    def check_line(self, line):
        if len(set(line)) == 1 and line[0] != -1:
            return True
        return False

    def move(self, row: int, col: int, player: int) -> int:

        self.m[row][col] = player
        ls_left = []
        ls_right = []
        for i in range(self.n):
            ls_right.append(self.m[i, i])
            ls_left.append(self.m[i, self.n-i-1])
            if self.check_line(self.m[i, :]) or self.check_line(self.m[:, i]):
                return player
        if self.check_line(ls_left) or self.check_line(ls_right):
            return player
        # print(self.m)
        return 0


if __name__ == '__main__':
    t = TicTacToe(3)
    print(t.move(0, 0, 1))
    print(t.move(0, 2, 2))
    print(t.move(2, 2, 1))
    print(t.move(1, 1, 2))
    print(t.move(2, 0, 1))
    print(t.move(1, 0, 2))
    print(t.move(2, 1, 1))
    #
    # t = TicTacToe(2)
    # print(t.move(0, 1, 1))
    # print(t.move(1, 1, 2))
    # print(t.move(1, 0, 1))
