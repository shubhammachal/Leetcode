class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = {}
        for char in text:
            freq[char] = freq.get(char, 0) + 1
            
        target = "balloon"
        req_freq = {}
        for char in target:
            req_freq[char] = req_freq.get(char, 0) + 1
        
        min_balloons = float('inf')
        for char, count in req_freq.items():
            if char in freq:
                min_balloons = min(min_balloons, freq[char] // count)
            else:
                return 0
        return min_balloons
        
        