class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        #only lowercase english letters
        freq_map = [0] * 26
        for char in s:
            freq_map[ord(char) - ord('a')] += 1
        odd_count = 0
        for i in range(len(freq_map)):
            if freq_map[i] % 2 == 1:
                odd_count += 1
        #if odd length string, can have one element with odd count
        #even length string can have 0 element with odd count
        return odd_count <= 1