class Solution:
    def trailingZeroes(self, n: int) -> int:
        c = 0
        while n >= 5:
            n = int(n/5)
            c += n
        return c