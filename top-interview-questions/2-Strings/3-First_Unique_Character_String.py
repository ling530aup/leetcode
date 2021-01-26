from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        ls = []
        for key in counter:
            if counter[key] == 1:
                ls.append(key)
        ls = set(ls)
        
        for index, char in enumerate(s):
            if char in ls:
                return index
        return -1
        
