class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k:
            min_index = nums.index(min(nums))
            nums[min_index] *= multiplier
            k -= 1
        return nums