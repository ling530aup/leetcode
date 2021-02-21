def lengthOfLongestSubstring(s: str) -> int:
    if not s:
        return 0
    left = 0
    lookup = set()
    max_len = 0
    for right in range(len(s)):
        while s[right] in lookup:
            lookup.remove(s[left])
            left += 1
        max_len = max(max_len, right - left + 1)
        lookup.add(s[right])
    return max_len


if __name__ == '__main__':
    assert lengthOfLongestSubstring("abcabcbb") == 3
    assert lengthOfLongestSubstring("bbbb") == 1
