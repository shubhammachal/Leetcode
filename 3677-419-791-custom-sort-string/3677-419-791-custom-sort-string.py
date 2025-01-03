from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        #count the occurence of each character in s
        
        counts = Counter(s)
        res = []
        
        # append characters from s in the order specified by order.
        
        for char in order:
            if char in counts:
                res.append(char * counts[char])
                del counts[char] #deleted from counts to append remaining elements from s
        
        #append remaining elements from s
        
        for char, count in counts.items():
            res.append(char * count)
        return "".join(res)
                