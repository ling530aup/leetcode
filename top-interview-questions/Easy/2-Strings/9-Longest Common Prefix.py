class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        max_len = 999
        for w in strs:
            if len(w) <max_len:
                max_len = len(w)
                
        if max_len == 0:
            return ""
        
        for i in range(0, max_len):
            for item in strs:
                if item[i] !=strs[0][i]:
                    if i==0:
                        return ""
                    else:
                        return strs[0][:i]

        return strs[0][:max_len]
