class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        #sliding window
        n = len(nums)
        inc_max = dec_max = 1
        left_inc = left_dec = 0
        
        #check for increasing seq
        for right in range(1,n):
            if nums[right] > nums[right-1]:
                inc_max = max(inc_max, right - left_inc + 1)
            else:
                left_inc = right
        #for decreasing seq
            if nums[right] < nums[right - 1]:
                dec_max = max(dec_max, right - left_dec + 1)
            else:
                left_dec = right
        return max(inc_max, dec_max)


        