class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        # 处理符号
        if s == '':
            return 0
        flag = 1
        if s[0] == '-':
            flag = -1
        # 如果有符号跳1格
        if s[0] in ['-', '+']:
            s = s[1:]
        i = 0
        for i in range(len(s)):
            if not s[i].isnumeric():
                break
        if len(s)!=0 and (not s[i].isnumeric()):
            s = s[:i]

        if s == '':
            return 0
        rt = int(s) * flag
        if rt > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if rt < -2 ** 31:
            return -2 ** 31
        return rt
