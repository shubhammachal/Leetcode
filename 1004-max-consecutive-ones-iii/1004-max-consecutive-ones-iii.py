class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = 0
        long_seq = 0
        zeros = 0
        #calculate number of zeros
        while right < len(nums):
            if nums[right] == 0:
                zeros += 1
            #shrink window size and if nums[left] == 0, reduce count of zeros
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            long_seq = max(long_seq, right - left + 1)
            right += 1
        return long_seq