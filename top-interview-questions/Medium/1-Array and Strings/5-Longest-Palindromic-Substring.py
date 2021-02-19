def longestPalindrome(s) -> int:
    longest_p = 1
    for index, c in enumerate(s):
        length = min(index, len(s) - index - 1)
        flag = 1
        for gap in range(length + 1):
            if s[index - gap] != s[index + gap]:
                break
            if gap < length and s[index - gap] != s[index + gap + 1]:
                flag = 1
                break
        longest_p = max(longest_p, gap * 2 + flag)
    return longest_p


if __name__ == '__main__':
    print(longestPalindrome('aaaa'))
    assert True
