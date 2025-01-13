class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        #use two pointers, total 3 scenarios
        no_op = 0
        left = 0
        right = len(nums) - 1
        while left < right:
            #scenrio 1
            if nums[left] == nums[right]:
                left += 1
                right -= 1
            #scenrio 2
            elif nums[left] < nums[right]:
                nums[left + 1] += nums[left]
                no_op += 1
                left += 1
            #scenrio. 3
            elif nums[right] < nums[left]:
                nums[right - 1] += nums[right]
                no_op += 1
                right -= 1
        return no_op
