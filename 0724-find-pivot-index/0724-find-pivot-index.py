class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums) 
        left_sum = [nums[0]]
        for i in range(1,n):
            left_sum.append(left_sum[-1] + nums[i])

        right_sum = [0] * n
        right_sum[-1] = nums[n-1]
        
        for i in range(n-2,-1,-1):
            right_sum[i] = (right_sum[i+1] + nums[i])
        
        for i in range(len(nums)):
            if left_sum[i] == right_sum[i]:
                return i
        return -1
            
        
            