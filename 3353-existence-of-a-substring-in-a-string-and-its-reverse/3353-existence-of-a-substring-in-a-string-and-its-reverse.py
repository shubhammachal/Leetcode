class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        rev = s[::-1]
        n = len(s) 
        if len(set(s)) == n:
            return False
        left, right = 0,1
        while right <= n - 1:
            if s[left:right+1] in rev:
                return True
            left += 1
            right += 1
        return False
        
