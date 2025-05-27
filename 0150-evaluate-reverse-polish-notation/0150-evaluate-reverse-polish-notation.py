class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #set operators
        operations = {
                '+': lambda a, b: a + b,
                '-': lambda a, b: a - b,
                '*': lambda a, b: a * b,
                '/': lambda a, b: int(a / b)
        }

        #initialize stack and res
        stack = []
        res = 0
        for char in tokens:
            if char not in operations:
                stack.append(int(char))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                res = operations[char](operand1, operand2)

                stack.append(res)
        return stack.pop()