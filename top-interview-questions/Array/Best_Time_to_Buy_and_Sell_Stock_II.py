def maxProfit(prices):
    total = 0
    for i in range(len(prices) - 1):
        if prices[i + 1] > prices[i]:
            total += prices[i + 1] - prices[i]
    return total


if __name__ == '__main__':
    assert maxProfit([7, 1, 5, 3, 6, 4])
    print('------')
