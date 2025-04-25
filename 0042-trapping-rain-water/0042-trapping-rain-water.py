class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 2:
            return 0
        n = len(height)
        left, right = 0, n - 1
        left_max, right_max = height[left], height[right]
        
        total_water = 0
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(height[left], left_max)
                total_water += left_max - height[left]
            else:
                right -= 1
                right_max = max(height[right], right_max)
                total_water += right_max - height[right]
        return total_water