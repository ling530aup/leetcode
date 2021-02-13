'''
242. 有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
思路 ： 
1. 注意为什么不嫩够用 Set？ Set('aaaaaab') = Set('ba')
2. Counter 比 Sorted 更快一些
'''
from collections import Counter


def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


if __name__ == '__main__':
    assert isAnagram('anagram', 'nagaram')
    assert not isAnagram('rat', 'car')
