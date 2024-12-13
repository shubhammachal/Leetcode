class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        target = n-1
        for i in range(n-1, -1, -1):
            if i + nums[i] >= target:
                target = i
        return target == 0