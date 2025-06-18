class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        min_bound = float('-inf')
        stack = []

        for element in preorder:
            while stack and stack[-1] < element:
                min_bound = stack.pop()
            if element <= min_bound:
                return False
            stack.append(element)
        return True