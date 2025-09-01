class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        n = len(s)
        if n < 2:
            return False

        for i in range(n-1):
            if s[i] == s[i+1]:
                return True
        substrings = set()
        for i in range(n-1):
            substrings.add(s[i : i+2])

        for substring in substrings:
            reversed_substring = substring[::-1]
            if reversed_substring in substrings:
                return True
        return False

        