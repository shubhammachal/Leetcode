class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        n = len(word)
        m = len(abbr)
        i = j = 0
        
        while i < n and j < m:
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif not abbr[j].isdigit() or abbr[j] == "0":
                return False
            else:
                start = j
                while j < m and abbr[j].isdigit():
                    j += 1
                num = int(abbr[start:j])
                i += num
                if i > n:  # Changed from num > n-1
                    return False
        
        return i == n and j == m