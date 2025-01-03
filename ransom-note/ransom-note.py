from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_freq = Counter(ransomNote)
        for char in magazine:
            if char in ransom_freq:
                ransom_freq[char] -= 1
        for char, count in ransom_freq.items():
            if count > 0:
                return False
        return True