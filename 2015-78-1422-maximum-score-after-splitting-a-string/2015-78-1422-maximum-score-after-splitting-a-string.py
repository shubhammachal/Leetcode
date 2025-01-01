from collections import Counter
class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        for i in range(len(s) - 1):
            curr = 0
            for j in range(i+1):
                if s[j] == "0":
                    curr += 1
            for j in range(i+1, len(s)):
                if s[j] == '1':
                    curr += 1
            if curr > max_score:
                max_score = curr
        return max_score