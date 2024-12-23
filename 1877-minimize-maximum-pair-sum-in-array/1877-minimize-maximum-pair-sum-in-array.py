class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = []
        n = len(nums)
        max_sum = 0 
        for i in range(n//2):
            curr_sum = nums[i] + nums[n-1-i]
            if curr_sum > max_sum:
                max_sum = curr_sum
        return max_sum
        
            
            