class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = [nums[0]]
        for i in range(1,len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[-1])
            
        return max(1, 1 - min(prefix_sum))