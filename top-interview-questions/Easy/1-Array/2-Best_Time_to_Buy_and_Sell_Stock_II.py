
def maxProfit(prices):
    '''
        满足局部最优解合并就是全局最优解的特点。 贪心算法。  直接计算可以产生利润的相邻时间点， 把利润累加
    '''
    total = 0
    for i in range(len(prices) - 1):
        if prices[i + 1] > prices[i]:
            total += prices[i + 1] - prices[i]
    return total


if __name__ == '__main__':
    assert maxProfit([7, 1, 5, 3, 6, 4])
    print('------')
