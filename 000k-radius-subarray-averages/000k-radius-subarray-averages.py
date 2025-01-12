class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * n
        
        #edge cases
        if n < k:
            return res
        if k == 0:
            return nums
        #calculate 1st window sum which is from 0 to 2k + 1
    
        curr_sum = sum(nums[:2 * k +1])
            
        # only these indices will contain average ( from k to n - k)
        for i in range(k, n-k):
            res[i] = curr_sum // (2 * k + 1)
            
            #update the sum for the next window
            if i + k + 1 < n:
                curr_sum += nums[i + k + 1] - nums[i-k]
        return res
    
        
        