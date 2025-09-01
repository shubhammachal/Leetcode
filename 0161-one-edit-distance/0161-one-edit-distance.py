class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if abs(n - m) > 1:
            return False
        i = 0 
        #will find the first index where the characters are different
        while i < n and i < m and s[i] == t[i]:
            i += 1
        #if we reach the end of both the strings and can't find such character,
        #return False
        if i == n and i == m:
            return False
        #if lengths are not equal and diff char found is at index i
        #we will compare rest of the characters are same or not
        if n < m:
            return s[i:] == t[i+1:]
        elif n > m:
            return s[i+1:] == t[i:]
        #if lengths are equal and diff char is at index i
        #check if rest of the string is same
        else:
            return s[i+1:] == t[i+1:]


