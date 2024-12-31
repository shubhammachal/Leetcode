class Solution:
    def repeatedCharacter(self, s: str) -> str:
        for i in range(len(s)):
            char = s[i]
            for j in range(i):
                if s[j] == s[i]:
                    return s[j]