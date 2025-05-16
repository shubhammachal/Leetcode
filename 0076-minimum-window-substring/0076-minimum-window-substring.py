from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #initialize freq counters
        freq_t = Counter(t)
        freq_win = Counter()

        #initialize pointers
        left = 0
        required = len(freq_t)
        formed = 0

        #variables to store the result
        result_start = 0
        min_len = float('inf')

        #slide the window
        for right in range(len(s)):
            char = s[right]
            freq_win[char] += 1

            #check if this char helps satisfy the cond
            if char in freq_t and freq_win[char] == freq_t[char]:
                formed += 1
            
            #if we have a valid window, shrink it
            while formed == required and left <= right:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result_start = left

                char_left = s[left]
                freq_win[char_left] -= 1

                if char_left in freq_t and freq_win[char_left] < freq_t[char_left]:
                    formed -= 1
                left += 1
        return s[result_start:result_start + min_len] if min_len != float('inf') else ""


