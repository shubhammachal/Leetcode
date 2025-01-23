class Solution:
    def countSubstrings(self, s: str) -> int:
        def countPalindrome(s, left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        count = 0
        for i in range(len(s)):
            #for odd length palindrome
            count += countPalindrome(s, i, i)
            #for even length palindrome
            count += countPalindrome(s, i, i+1)
        return count

        
        