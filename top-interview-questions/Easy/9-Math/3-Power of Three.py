class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        a = 1
        while a<n:
            a = a*3
        return a == n
