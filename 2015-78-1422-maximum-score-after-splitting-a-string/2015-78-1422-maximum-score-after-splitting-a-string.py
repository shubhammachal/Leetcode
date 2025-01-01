from collections import Counter
class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        ones = s.count('1')
        zeros = 0
        for i in range(len(s) - 1):
            if s[i] == '1':
                ones -= 1
            else:
                zeros += 1
            max_score = max(max_score, ones + zeros)
        return max_score
                