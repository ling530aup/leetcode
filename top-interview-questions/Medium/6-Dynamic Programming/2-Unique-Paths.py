class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for i in range(n):
            dp.append([-1] * m)

        for i in range(m):
            dp[n - 1][m - 1 - i] = 1

        for i in range(n):
            dp[n - 1 - i][m - 1] = 1

        for col in range(m - 2, -1, -1):
            for raw in range(n - 2, -1, -1):
                dp[raw][col] = dp[raw + 1][col] + dp[raw][col + 1]

        return dp[0][0]