class Solution:
    def partitionString(self, s: str) -> int:
        result = 1 #to also include last char, otherwise if initialized to 0, it won't take last char into account an dsince string is always non empty
        hash_set = set()
        for c in s:
            if c in hash_set:
                result +=1
                #clear hash_set to store char of another substring
                hash_set = set()
            hash_set.add(c)
        return result

        