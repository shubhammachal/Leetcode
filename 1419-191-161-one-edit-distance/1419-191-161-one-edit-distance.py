class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1:
            return False
        i = 0 
        while i < len(s) and i < len(t) and s[i] == t[i]:
            i += 1
        if i == len(s) and i == len(t):
            return False
        
        if len(s) < len(t):
            return s[i:] == t[i+1:]
        elif len(s) > len(t):
            return s[i+1:] == t[i:]
        else:
            return s[i+1:] == t[i+1:]