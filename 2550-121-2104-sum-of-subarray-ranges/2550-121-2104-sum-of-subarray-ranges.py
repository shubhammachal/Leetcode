class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        sums = 0 
        if len(nums) == 1:
            return 0
        for i in range(len(nums)):
            min_val = float('inf')
            max_val = float('-inf')
            for j in range(i, len(nums)):
                min_val = min(min_val, nums[j])
                max_val = max(max_val, nums[j])
                sums += max_val - min_val
        return sums      