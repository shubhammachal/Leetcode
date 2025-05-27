class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #edge case
        if len(tokens) == 1:
            return int(tokens[0])
        #set operators
        operators = set(['+', '-', '*', '/'])
        #initialize stack and res
        stack = []
        res = 0
        for char in tokens:
            if char not in operators:
                stack.append(int(char))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if char == '+':
                    res = operand1 + operand2
                elif char == '-':
                    res = operand1 - operand2
                
                elif char == '*':
                    res = operand1 * operand2
                elif char == '/':
                    res = int(operand1 / operand2)
                stack.append(res)
        return res