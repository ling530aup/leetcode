from collections import Counter
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return  Counter(bin(x ^ y)[2:])['1']
   
