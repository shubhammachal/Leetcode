class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        indices_to_remove = set()
        for index, char in enumerate(s):
            if char not in "()":
                continue
            if char == "(":
                stack.append(index)
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