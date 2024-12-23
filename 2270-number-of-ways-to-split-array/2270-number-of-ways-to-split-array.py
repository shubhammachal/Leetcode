class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix_sum = [nums[0]]
        count = 0
        for i in range(1, len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[-1])

        for i in range(len(nums) - 1):
            left_section = prefix_sum[i]
            right_section = prefix_sum[-1] - prefix_sum[i]
            if left_section >= right_section:
                count += 1
        return count