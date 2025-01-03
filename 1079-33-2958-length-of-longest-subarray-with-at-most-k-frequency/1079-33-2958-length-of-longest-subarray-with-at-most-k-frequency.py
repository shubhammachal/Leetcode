from collections import Counter
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = right = 0
        ans = 0
        freq = Counter()

        for right in range(len(nums)):
            freq[nums[right]] += 1
            while freq[nums[right]] > k:
                
                freq[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans

