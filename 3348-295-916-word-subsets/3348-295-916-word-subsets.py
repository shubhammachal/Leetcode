from collections import Counter
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        #idea is to combine the freq of all the chars of words2 into a single freq which will be max freq. 
        max_freq = Counter()
        for word in words2:
            word_count = Counter(word)
            for char,freq in word_count.items():
                max_freq[char] = max(freq, max_freq[char])
        res = []
        for word in words1:
            words1_freq =  Counter(word)
            if all(words1_freq[char] >= freq for char, freq in max_freq.items()):
                res.append(word)
        return res


