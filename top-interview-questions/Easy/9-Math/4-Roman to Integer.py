from collections import deque
class Solution:
    def romanToInt(self, s: str) -> int:
        _dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100,'D':500, 'M':1000}
        q = deque(s)
        count = 0
        while q:
            top = q.popleft()
            if len(q)==0 or _dict[top] >= _dict[q[0]]:
                count +=  _dict[top]
            if len(q)!=0 and _dict[top] < _dict[q[0]]:
                count -= _dict[top]
        return count
        
