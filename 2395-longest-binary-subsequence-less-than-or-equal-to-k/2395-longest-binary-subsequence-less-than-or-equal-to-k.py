class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        decimal_value = 0
        long_sub = 0
        rev_s = s[::-1]
        for i in range(n):
            if rev_s[i] == '1':
                decimal_value += 2 ** i
                if decimal_value <= k:
                    long_sub += 1
                    continue
            else:
                long_sub += 1
        return long_sub