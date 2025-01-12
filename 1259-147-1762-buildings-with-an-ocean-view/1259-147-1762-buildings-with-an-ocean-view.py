class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # constraint is iteration from left to right
        # decreasing monotonic stack: if the current height is greater than or equal to the top of the stack
        # pop from the stack and add current height to maintain the decreasing order
        # add the current index to the stack
        stack = []
        for i in range(len(heights)):
            while stack and heights[i] >= heights[stack[-1]]:
                stack.pop()
            stack.append(i)
        return stack

            