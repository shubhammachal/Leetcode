class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = []
        n = len(nums)
        left = 0
        right = n - 1
        while left < right:
            res.append([nums[left], nums[right]])
            left += 1
            right -= 1
        sums = [sum(pair) for pair in res]
        return max(sums)
        
            
            