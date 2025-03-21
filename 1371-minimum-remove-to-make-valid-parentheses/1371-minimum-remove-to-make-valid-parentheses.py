class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        indices_to_remove = set()
        for index, char in enumerate(s):
            if char not in "()":
                continue
            if char == "(":
                stack.append(index)
            #if stack is empty and we have closing parentheses, means
            #it's not valid as closing parentheses can't be there before opening one
        
            elif not stack:
                indices_to_remove.add(index)
            else:
                stack.pop()
    
        indices_to_remove = indices_to_remove.union(set(stack))
        print(indices_to_remove)
        string_list = []
        for index, char in enumerate(s):
            if index not in indices_to_remove:
                string_list.append(char)
        return "".join(string_list)