class Solution:
    def sumNums(self, n: int) -> int:
        # 短路，and:最终结果成立时，返回后者;or:最终结果成立时，返回前者
        return n and (n + self.sumNums(n-1))

# 这题没有意义
