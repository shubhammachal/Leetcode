class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) == 1:
            return s
            
        stack = []
        for char in s:
            if stack and abs(ord(char) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
                