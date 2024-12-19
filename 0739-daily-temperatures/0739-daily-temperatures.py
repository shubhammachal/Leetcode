class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                popped_index = stack.pop()
                ans[popped_index] = i - popped_index
            stack.append(i)
        return ans