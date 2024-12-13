class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result =  [1] * n
        prefix = 1
        for i in range(n):
            result[i] = prefix #store prefix in the result 
            prefix *= nums[i] #update prefix by multiplying with nums[i]

        suffix = 1
        for i in range(n-1, -1, -1):
            result[i] *= suffix #multiplying prefix stored in the result with suffix
            suffix *= nums[i] #update suffix by multiplying with nums[i]
        return result
    
#time complexity O(n)
#space complexity O(1)