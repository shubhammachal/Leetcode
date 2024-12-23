class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count_zeros = 0
        left = 0
        long_seq = 0
        right = 0
        while right < len(nums):
            if nums[right] == 0:
                count_zeros += 1
                
            while count_zeros > k:
                if nums[left] == 0:
                    count_zeros -= 1
                left += 1
            long_seq = max(long_seq, right - left + 1)
            right += 1
        return long_seq
            