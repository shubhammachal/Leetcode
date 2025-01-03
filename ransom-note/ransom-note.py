from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_freq = Counter(ransomNote)
        magazine_freq = Counter(magazine)
        return all(ransom_freq[char] <= magazine_freq[char] for char in ransom_freq)