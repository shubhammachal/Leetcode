class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        n = len(part)
        for char in s:
            stack.append(char)
            if "".join(stack[-n:]) == part:
                for _ in range(n):
                    stack.pop()
        return "".join(stack)
