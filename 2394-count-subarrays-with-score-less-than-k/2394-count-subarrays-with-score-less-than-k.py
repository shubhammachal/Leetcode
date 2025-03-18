class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        curr_sum = 0
        count = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            curr_length = (right - left) + 1
            curr_score = curr_sum * curr_length

            #shrink window
            while curr_score >= k and left <= right:
                curr_sum -= nums[left]
                left += 1
                curr_length = right - left + 1
                curr_score = curr_sum * curr_length
            count += (right - left ) + 1
        return count
