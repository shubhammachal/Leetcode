class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_nums = n *(n+1)/2
        curr_sum = 0
        for num in nums:
            curr_sum += num
        return int(sum_nums - curr_sum)