from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        #frequenct of characters in text
        text_counts = Counter(text)
        
        # required freq of each char in balloon
        target_counts = Counter("balloon")
        

        return min(text_counts[char] // count for char, count in target_counts.items())
