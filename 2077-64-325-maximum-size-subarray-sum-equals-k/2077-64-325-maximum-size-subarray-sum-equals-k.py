class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        hash_map = {0:-1}
        max_size = 0
        curr_sum = 0
        for index, num in enumerate(nums):
            curr_sum += num
            if curr_sum - k in hash_map:
                max_size = max(max_size, index - hash_map[curr_sum - k])
            if curr_sum not in hash_map:
                hash_map[curr_sum] = index
        return max_size 