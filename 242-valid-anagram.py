'''
Using sort: 
return sorted(s) == sorted(t)
Time complexity: O(n log n), where n is the length of the strings
Space complexity: O(1) if using in-place sorting, O(n) if creating new sorted strings'''

#Using Hashmap

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if lengths are equal
        if len(s) != len(t):
            return False  # anagrams must be of equal lengths
        
        # Initialize empty dictionaries to store character counts
        countS, countT = {}, {}
        
        # Count occurrences of each character in both strings
        for i in range(len(s)):
            # Increment count for character in s, default to 0 if not present
            countS[s[i]] = 1 + countS.get(s[i], 0)
            # Increment count for character in t, default to 0 if not present
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        # Compare character counts
        for char in countS:
            # If counts don't match, strings are not anagrams
            if countS[char] != countT.get(char, 0):
                return False
        
        # If all checks pass, strings are anagrams
        return True

# Time complexity: O(n), where n is the length of the strings
# Space complexity: O(n), as there are at most 26 lowercase English letters