class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        left_sum = right_sum = 0
        count = 0
        right_sum = sum(nums)
        for i in range(len(nums) - 1):
            left_sum += nums[i]
            right_sum -= nums[i]
            if left_sum >= right_sum:
                count += 1
        return count