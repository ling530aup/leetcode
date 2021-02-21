def longestPalindrome(s) -> int:
    if len(s) == 1:
        return s

    longest_p = 0
    res = ''
    for center in range(len(s) - 1):
        length = 0

        while center - length >= 0 and center + length < len(s):
            if s[center - length] != s[center + length]:
                break
            else:
                if longest_p < length * 2 + 1:
                    res = s[center - length: center + length + 1]
                    longest_p = length * 2 + 1
            length += 1

        # there center is left center
        length = 0
        while center - length >= 0 and center + 1 + length < len(s):
            if s[center - length] != s[center + 1 + length]:
                break
            else:
                if longest_p < length * 2 + 2:
                    res = s[center - length: center + length + 2]
                    longest_p = length * 2 + 2
            length += 1
    return res


if __name__ == '__main__':

    assert longestPalindrome('babad') == 'bab'
    assert longestPalindrome('a') == 'a'
    assert longestPalindrome('aa') == 'aa'
    assert longestPalindrome('aaa') == 'aaa'
    assert longestPalindrome('aaaa') == 'aaaa'
    assert longestPalindrome('caba') == 'aba'
