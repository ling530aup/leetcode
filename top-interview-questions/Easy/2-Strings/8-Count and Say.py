def desc(string):
    if string == '1':
        return '1'
    rt = []
    count = 1
    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            rt.append(str(count))
            rt.append(str(string[i]))
            count = 1
        else:
            count += 1
    rt.append(str(count))
    rt.append(str(string[len(string) - 1]))
    return ''.join(rt)

class Solution:
    def countAndSay(self, n) -> str:
        if n == 1:
            return '1'
        rt = '11'
        for i in range(n-2):
            rt = desc(rt)
        return rt
