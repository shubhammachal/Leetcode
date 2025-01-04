class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        s = list(s)
        #check edge cases
        if len(s) != len(goal):
            return False
        #if s equals goal and s contains one duplicate, return true e.g. aa return true ab return False
        if s == list(goal):
            seen = set()
            for char in s:
                if char in seen:
                    return True
                seen.add(char)
            return False
        #find mismatched indices
        mismatched = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                mismatched.append(i)
        if len(mismatched) != 2:
            return False
        
        i, j = mismatched
        return s[i] == goal[j] and s[j] == goal[i]
        
                
            