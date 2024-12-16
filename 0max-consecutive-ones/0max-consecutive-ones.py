class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        
        count = 0
        for right in range(len(nums)):
            if nums[right] == 0 :
                left = right + 1
            count = max(count, right - left + 1)
        return count
            
        