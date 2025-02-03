class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        #brute force
        max_len = 0
        n = len(nums)
        #strcitly increasing
        for i in range(n):
            curr_len = 1
            for j in range(i+1, n):
                if nums[j] > nums[j-1]: #increasing seq
                    curr_len += 1
                else:
                    break
            max_len = max(curr_len, max_len)
        #strictl decreasing
        for i in range(n):
            curr_len = 1
            for j in range(i+1, n):
                if nums[j] < nums[j-1]: #strictly decreasing
                    curr_len += 1
                else:
                    break
            max_len = max(curr_len, max_len)
        return max_len



