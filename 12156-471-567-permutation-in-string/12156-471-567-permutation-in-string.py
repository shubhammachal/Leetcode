from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        sorted_s1 = sorted(s1)
        window_size = n
        for i in range(len(s2)):
            sorted_wind = sorted(s2[i: i + n])
            if sorted_wind == sorted_s1:
                return True
        return False


