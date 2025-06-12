class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_diff = float('-inf')
        n = len(nums)
        for i in range(n):
            curr = nums[i]
            next = nums[(i + 1) % n]
            max_diff = max(max_diff,abs(curr - next) )
        return max_diff
