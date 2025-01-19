class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        from collections import defaultdict
        char_map = defaultdict(int)
        left = 0
        long_sub = 0
        for right in range(len(s)):
            char_map[s[right]] += 1

            while len(char_map) > k:
                char_map[s[left]] -= 1
                if char_map[s[left]] == 0:
                    del char_map[s[left]]
                left += 1

            long_sub = max(long_sub, right - left + 1)
        return long_sub