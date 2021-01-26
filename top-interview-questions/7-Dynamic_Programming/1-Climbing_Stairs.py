class Solution:
    def climbStairs(self, n: int) -> int:
        ls = [1,2]
        if n > 2:
            for i in range(n-2):
                ls.append(ls[-1] + ls[-2])
            return ls[-1]
        return ls[n-1]
      
