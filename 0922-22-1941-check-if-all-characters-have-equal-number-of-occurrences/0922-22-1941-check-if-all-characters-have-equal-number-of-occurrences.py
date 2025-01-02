from collections import defaultdict
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = defaultdict(int)
        for char in s:
            freq[char] += 1
        values = set(freq.values())
        return len(values) == 1