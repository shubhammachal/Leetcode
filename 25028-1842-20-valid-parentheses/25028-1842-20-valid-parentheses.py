class Solution:
    def isValid(self, s: str) -> bool:
        hm = {')':'(', '}':'{', ']':'['}
        stack = []
        #if the stack is empty and 1st char is a closing parneteses, then string can 
        #never be valid so we will return false 
        for char in s:
            #if statement checks for keys in hm
            if char in hm:
                #checks for non empty stack and top is matching parenteses with current char
                #if it does pop(means cancel those two parentheses)
                if stack and stack[-1] == hm[char]:
                    stack.pop()
                #if stack is empty and char in hm
                # means first char is a closing parentheses
                # immediately return False
                else:
                    return False
            # if char not in hm, means char is not a closing parentheses
            #char is an opening parentheses and add as many opening parnetheses as we want
            else:
                stack.append(char)
        # if stack is empty(every closing parentheses cancels out openeing parentheses)
        #return True otherwise False
        return True if not stack else False


        