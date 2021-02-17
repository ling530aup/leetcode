def lengthOfLongestSubstring(s: str) -> int:
    _dict = {}
    left = 0
    if not s:
        print('@@@@')
        return 0

    max_substr_len = 1
    for right, char in enumerate(s):
        if char in _dict:
            left = _dict[char]
        _dict[char] = right
        max_substr_len = max(right - left, max_substr_len)
    return max_substr_len + int(s[left] != s[right])


if __name__ == '__main__':
    assert lengthOfLongestSubstring("abcabcbb") == 3
    assert lengthOfLongestSubstring("bbbb") == 1
    print(lengthOfLongestSubstring('aab'))
    print(lengthOfLongestSubstring('bbbb'))
