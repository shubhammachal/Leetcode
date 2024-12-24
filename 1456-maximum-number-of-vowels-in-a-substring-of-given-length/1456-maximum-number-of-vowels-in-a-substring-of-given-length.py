class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        #edge case handeling
        if k <= 0 or k > len(s):
            return 0
        vowels = set('aeiou') # set for O(1) lookup, in case of list O(n) lookup
        s = s.lower()
        left = 0
        count_vowels = 0
        max_count = 0
        
        for right in range(len(s)):
            if s[right] in vowels:
                count_vowels += 1
                
            if (right - left + 1) > k:
                #if window size > k, check if left is vowel, if so reduce count and increment left anyway
                if s[left] in vowels:
                    count_vowels -= 1
                left += 1
            if (right - left + 1) == k:
                #if window size equals k, update max_count
                max_count = max(max_count, count_vowels)
        return max_count
                    