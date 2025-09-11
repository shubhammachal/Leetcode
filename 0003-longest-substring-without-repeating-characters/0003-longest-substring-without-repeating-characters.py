class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        long_sub = 0
        left = 0
        for right in range(len(s)):
            if s[right] in char_map:
                left = max(left, char_map[s[right]] + 1)
            char_map[s[right]] = right
            long_sub = max(long_sub, right - left + 1)
        return long_sub