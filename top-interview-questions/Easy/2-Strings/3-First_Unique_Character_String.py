'''
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。


'''

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
        
