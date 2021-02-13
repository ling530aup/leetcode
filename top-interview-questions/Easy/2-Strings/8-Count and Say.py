'''
38. 外观数列 countAndSay
前五项如下：
1.     1
2.     11
3.     21
4.     1211
5.     111221
'''


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


def countAndSay(n) -> str:
    if n == 1:
        return '1'
    rt = '11'
    for i in range(n - 2):
        rt = desc(rt)
    return rt

if __name__ == '__main__':
    countAndSay(4) == '1211'
