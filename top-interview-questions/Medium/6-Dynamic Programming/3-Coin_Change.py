from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    for index, item in enumerate(coins):
        if item ==



if __name__ == '__main__':
    assert coinChange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert coinChange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert coinChange([], 0) == [-1, -1]
