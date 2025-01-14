class Solution:
    def removeDuplicates(self, s: str) -> str:
        # will use stack to push char and 
        # compare the top with the curr_char
        # if both are same, pop

        stack = []
        for char in s:
            if stack and char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)