class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if abs(n - m) > 1:
            return False
        i = 0 

        while i < n and i < m and s[i] == t[i]:
            i += 1
 
        if i == n and i == m:
            return False

        if n < m:
            return s[i:] == t[i+1:]
        elif n > m:
            return s[i+1:] == t[i:]
        
        else:
            return s[i+1:] == t[i+1:]


