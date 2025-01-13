from collections import Counter
class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s)
        n = len(s)
        #edge case
        if n <= 2:
            return n
        #if freq is odd: can delete value - 2 elements
        #if freq is even: can delete value - 1 elements
        # and value should be greater than 2 to delete an element
        
        can_delete = sum((value - 2 if value % 2 == 0 else value - 1) for value in freq.values() if value > 2)
        return n - can_delete
        


