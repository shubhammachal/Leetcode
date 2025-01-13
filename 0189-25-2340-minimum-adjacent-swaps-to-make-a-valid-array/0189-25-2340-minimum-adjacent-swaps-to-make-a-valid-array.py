class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        min_idx = nums.index(min(nums))
        n = len(nums)

        max_idx = n-1
        for i in range(n-2,-1,-1):
            if nums[i] > nums[max_idx]:
                max_idx = i
        count = ((n - 1) - max_idx) + min_idx
        #overlap of 1 swap if min_idx is farther away from max_idx
        if min_idx > max_idx: 
            count -= 1
        return count