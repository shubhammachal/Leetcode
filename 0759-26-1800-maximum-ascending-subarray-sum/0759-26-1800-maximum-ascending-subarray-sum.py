class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        curr_sum = max_sum = nums[0]
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                curr_sum += nums[i]
            else:
                max_sum = max(curr_sum, max_sum)
                curr_sum = nums[i]
        return max(max_sum, curr_sum)

                
