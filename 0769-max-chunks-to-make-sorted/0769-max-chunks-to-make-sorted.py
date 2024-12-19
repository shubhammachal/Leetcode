class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        #monotonic stack
        
        stack = []
        for num in arr:
            curr_max = num
            while stack and stack[-1] > num:
                popped_element = stack.pop()
                curr_max = max(curr_max, popped_element)
            stack.append(curr_max)
         
        return len(stack)
