'''

Leetcode 14. 最长公共前缀
难度， 简单

最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""

https://leetcode-cn.com/problems/longest-common-prefix/

'''

from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""
    if len(strs) == 1:
        return strs[0]

    max_len = float('inf')
    for w in strs:
        if len(w) < max_len:
            max_len = len(w)

    if max_len == 0:
        return ""

    for i in range(0, max_len):
        for item in strs:
            if item[i] != strs[0][i]:
                if i == 0:
                    return ""
                else:
                    return strs[0][:i]

    return strs[0][:max_len]


if __name__ == '__main__':
    assert (["flower", "flow", "flight"]) == "fl"
    assert (["dog", "racecar", "car"]) == ""
