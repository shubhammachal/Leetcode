from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window_size = len(p)
        p_count = Counter(p)
        s_count = Counter()
        res = []
        left = 0
        for right in range(len(s)):
            s_count[s[right]] += 1  # Add the current character to the window
            
            # When window size exceeds required size, shrink it from the left
            if right - left + 1 > window_size:
                s_count[s[left]] -= 1
                if s_count[s[left]] == 0:
                    del s_count[s[left]]  # Remove char from dictionary to avoid clutter
                left += 1  # Move the left pointer

            # When the window size matches, compare frequency counts
            if right - left + 1 == window_size:
                if s_count == p_count:
                    res.append(left)
    
        return res