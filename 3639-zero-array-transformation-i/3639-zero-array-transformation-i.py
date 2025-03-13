class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        d_arr = [0] * len(nums)
        d_arr[0] = nums[0]
        for i in range(1,len(nums)):
            d_arr[i] = nums[i] - nums[i-1]
        
        for l,r in queries:
            d_arr[l] += -1
            if r + 1 < len(d_arr):
                d_arr[r+1] += 1

        for i in range(1, len(nums)):
            d_arr[i] += d_arr[i-1]
        return all(num <= 0 for num in d_arr)
