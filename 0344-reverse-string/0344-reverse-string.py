class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
    
        def reverse_helper(left, right):
            if left > right:
                return
            
            s[left], s[right] = s[right], s[left]
            reverse_helper(left + 1, right - 1)
            
        reverse_helper(0, len(s) - 1)
        