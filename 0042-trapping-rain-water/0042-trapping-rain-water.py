class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1,n):
            left_max[i] = max(left_max[i-1], height[i])
        right_max[n-1] = height[n-1]

        for i in range(n-2, -1 , -1):
            right_max[i] = max(right_max[i+1], height[i])
        
        trapped = 0
        for i in range(n):
            trapped_at_i = min(left_max[i], right_max[i]) - height[i]
            if trapped_at_i > 0:
                trapped += trapped_at_i
        return trapped


