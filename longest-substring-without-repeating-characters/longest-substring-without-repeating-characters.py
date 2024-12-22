class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        long_sub = 0 
        seen = set()
        
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            
            long_sub = max(long_sub, right - left + 1)
        return long_sub
        