from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        ransom_freq = Counter(ransomNote)
        for char in magazine:
            if char in ransom_freq:
                ransom_freq[char] -= 1
                if ransom_freq[char] == 0:
                    del ransom_freq[char]
                if not ransom_freq:
                    return True
        return False
        