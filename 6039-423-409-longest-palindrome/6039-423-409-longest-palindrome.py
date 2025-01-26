from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        has_odd = False
        count = 0
        for value in freq.values():
            # if freq of a character is even, we can use all of the frequencies
            if value % 2 == 0:
                count += value
            #if it is odd, we can use the even part which is value - 1
            else:
                count += value - 1
                has_odd = True
        #if there is one odd freq, can place that char in the center
        if has_odd == True:
            count += 1
        return count
