from collections import defaultdict 
#defualt dictionary used to avoid key errors. a default value is automatically returned or created for that key, eliminating the need to manually check for key existence.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        anagram_dict = defaultdict(list)
        for word in strs:
            sorted_word = str((sorted(word))) #sorted fn will give us list object, which are mutable and mutable data types can not be keys. so we can use str of tuple
            anagram_dict[sorted_word].append(word)
        for value in anagram_dict.values():
            res.append(value)
        return res