from collections import Counter
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        freq_s = Counter(s) #frequency count of given string
        required_freq = Counter(target) #required frequnecy to form target string
        minimum = float('inf')
        for char, count in required_freq.items():
            minimum = min(minimum, freq_s[char] // required_freq[char]) #find bottleneck char's frequency integer division by required freq of the char, which will be our answer
        return minimum
            