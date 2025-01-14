class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        #use stack, if char is # pop from stack
        stack_s = []
        stack_t = []
        for char in s:
            if stack_s and char == "#":
                stack_s.pop()
            elif char != "#":
                stack_s.append(char)
        for char in t:
            if stack_t and char == "#":
                stack_t.pop()
            elif char != "#":
                stack_t.append(char)
        return stack_s == stack_t