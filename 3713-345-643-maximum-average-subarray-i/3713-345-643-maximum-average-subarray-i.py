class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        curr_sum = 0
        #calculate current sum of the first window
        for i in range(k):
            curr_sum += nums[i]
        #maximum is the sum of the first window
        max_sum = curr_sum
        for right in range(k, len(nums)):
            curr_sum = curr_sum - nums[right - k] + nums[right]

            max_sum = max(max_sum, curr_sum)
        return max_sum / k 
        





    