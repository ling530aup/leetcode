from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    # if amount < min(coins):
    #     return 0

    dp = [0] + [float('inf')] * amount
    for i in range(1, amount + 1):
        for coin in coins:
            if coin < i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
            elif coin == i:
                dp[i] = 1
    # print(dp)
    return dp[amount] if dp[amount] <= amount else -1


if __name__ == '__main__':
    assert coinChange([2], 1) == -1
    assert coinChange([1], 1) == 1
    assert coinChange([1, 2, 5], 11) == 3
    assert coinChange([2], 3) == -1
    assert coinChange([1], 0) == 0
