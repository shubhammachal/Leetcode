class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        # 0 ^ 1 = 1
        # 1 ^ 0 = 1
        # 0 ^ 0 = 0
        # 1 ^ 1 = 0   
        #if xor of adjacent elements is 1 return True
        return all(nums[i] % 2 ^ nums[i+1] % 2 for i in range(n-1))