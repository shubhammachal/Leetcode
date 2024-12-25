class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums) - 1 
        left_sum = 0
        right_sum =sum(nums)
        for index, value in enumerate(nums):
            if left_sum == right_sum - nums[index]:
                return index
            left_sum += nums[index]
            right_sum -= nums[index]
        return -1
            