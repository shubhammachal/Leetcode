from collections import Counter
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) == k:
            return True
        if len(s) < k:
            return False
        freq = Counter(s)
        # if no of chars that have odd counts > k then it's not possible to construct palindrome 
        odd_count = sum(1 for value in freq.values() if value % 2 != 0)
        if odd_count > k:
            return False
        return True

        
        