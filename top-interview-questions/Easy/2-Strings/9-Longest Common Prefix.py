'''
Leetcode 14. 最长公共前缀
难度， 简单

最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""

https://leetcode-cn.com/problems/longest-common-prefix/

使用方法二，reduce，在leetcode提交超时
'''
from typing import List
from functools import reduce


def longestCommonPrefix_two_str(str1, str2):
    min_length = min(len(str1), len(str2))
    for i in range(min_length):
        if str1[i] != str2[i]:
            return str1[:i]
    return str1[:min_length]


def longestCommonPrefix_1(strs: List[str]) -> str:
    if not strs:
        return ""
    min_len = min(map(len, strs))
    for i in range(min_len):  # index for char
        for j in range(1, len(strs)):  # index for string
            if strs[j][i] != strs[0][i]:
                return strs[0][:i]
    return strs[0][:min_len]


def longestCommonPrefix_2(strs: List[str]) -> str:
    return reduce(longestCommonPrefix_two_str, strs)


if __name__ == '__main__':
    assert longestCommonPrefix_1(["flower", "flow", "flight"]) == "fl"
    assert longestCommonPrefix_1(["dog", "racecar", "car"]) == ""
    assert longestCommonPrefix_1(["aaa", "aaa", "aa"]) == "aa"

    assert longestCommonPrefix_2(["flower", "flow", "flight"]) == "fl"
    assert longestCommonPrefix_2(["dog", "racecar", "car"]) == ""
    assert longestCommonPrefix_2(["aaa", "aaa", "aa"]) == "aa"

    print('-----')