import numpy as np

def not_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1 or n==2:
            return 0
        
        n = n-1
        flag = np.ones(n+1, dtype=np.int)
        flag[0], flag[1] = 0, 0
        for i in range(2, n):
            if flag[i] == 1:  # and not_prime(i):
                for not_prim_index in range(2, int(n / i)+1):
                    flag[not_prim_index * i] = 0
        return flag.sum()
        
