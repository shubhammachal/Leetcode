class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        char_map = set()
        long_substr = 0
        
        for right in range(len(s)):
            while s[right] in char_map:
                char_map.remove(s[left])
                left += 1
            
            long_substr = max(long_substr, right - left + 1)
            char_map.add(s[right])
        return long_substr
            