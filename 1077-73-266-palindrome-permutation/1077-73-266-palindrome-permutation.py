from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()
        freq = Counter(s)
        odd_count = 0
        for key, value in freq.items():
            if freq[key] % 2 != 0:
                odd_count += 1
        return odd_count <= 1

    



        