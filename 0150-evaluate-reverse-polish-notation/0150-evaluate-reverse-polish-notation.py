class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b) 
        }

        res = 0
        stack = []
        for char in tokens:
            if char in operations:
                operand2 = stack.pop()
                operand1 = stack.pop()
                res = operations[char](operand1, operand2)
                stack.append(res)
            else:
                stack.append(int(char))
        return stack.pop()