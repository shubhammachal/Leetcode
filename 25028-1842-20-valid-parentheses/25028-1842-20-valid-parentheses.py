class Solution:
    def isValid(self, s: str) -> bool:
        hm = {')':'(', '}':'{', ']':'['}
        stack = []
        for char in s:
            if char in hm:
                if stack and stack[-1] == hm[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False


        