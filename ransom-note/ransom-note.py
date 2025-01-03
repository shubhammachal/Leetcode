from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Count character frequencies in both strings
        ransom_freq = Counter(ransomNote)
        magazine_freq = Counter(magazine)
        
        # Check if magazine has enough characters for the ransom note
        for char, count in ransom_freq.items():
            if magazine_freq[char] < count:
                return False
        return True
