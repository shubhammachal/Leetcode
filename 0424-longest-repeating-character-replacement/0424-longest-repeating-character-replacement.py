class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        most_freq = 0
        max_len = 0
        left = 0
        char_count = {}
        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            #window length - most freq char = number of replacements
            win_len = right - left + 1
            most_freq = max(most_freq, char_count[s[right]])
            if win_len - most_freq > k:
                char_count[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len