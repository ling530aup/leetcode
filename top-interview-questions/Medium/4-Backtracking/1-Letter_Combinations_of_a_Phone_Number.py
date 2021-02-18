from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        _dict = {'2': 'abc',
                 '3': 'edf',
                 '4': 'ghi',
                 '5': 'jkl',
                 '6': 'mno',
                 '7': 'pqrs',
                 '8': 'tuv',
                 '9': 'wxyz'}
        ls = []
        for num in digits:
            ls.append(tuple(_dict[num]))
        ls = tuple(ls)
        ans = list(product(*ls))
        ans = map(lambda x: ''.join(x), ans)
        return list(ans)

