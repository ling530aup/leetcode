class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        p_map = {')':'(','}':'{',']':'['}
        for i in s:
            if i in ['(','{','[']:
                stk.append(i)
            elif i in [')','}',']']:
                if stk and stk[-1] == p_map[i]:
                    stk.pop()
                else:
                    return False
        return not stk
 
