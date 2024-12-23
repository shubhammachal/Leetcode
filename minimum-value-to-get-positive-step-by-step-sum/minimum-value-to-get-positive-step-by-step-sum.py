class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # solve using prefix sum and prefix sum can be calculated on the fly
        
        total = 0
        min_val = 0
        for num in nums:
            total += num
            min_val = min(total, min_val)
        return 1 - min_val