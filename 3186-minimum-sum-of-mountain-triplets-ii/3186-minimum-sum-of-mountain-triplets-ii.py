class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_min  = [0] * n
        suffix_min = [0] * n
        prefix_min[0] = nums[0]
        suffix_min[n-1] = nums[n-1]

        for i in range(1, n):
            prefix_min[i] = min(prefix_min[i-1], nums[i])

        for i in range(n-2, -1, -1):
            suffix_min[i] = min(suffix_min[i+1], nums[i])
        
        min_sum = float('inf')
        for i in range(1, n-1):
            if nums[i] > prefix_min[i] and nums[i] > suffix_min[i]:
               min_sum = min(min_sum, nums[i] + prefix_min[i] + suffix_min[i])
               
        return min_sum if min_sum != float('inf') else -1