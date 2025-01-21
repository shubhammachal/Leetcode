from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window_size = len(p)
        p_count = Counter(p)
        s_count = Counter(s[:window_size - 1])
        res = []
        left = 0
        for right in range(window_size - 1, len(s)):
            s_count[s[right]] += 1

            if s_count == p_count:
                res.append(left)
            
            s_count[s[left]] -= 1
            if s_count[s[left]] == 0:
                del s_count[s[left]] 
            left += 1
        return res

    