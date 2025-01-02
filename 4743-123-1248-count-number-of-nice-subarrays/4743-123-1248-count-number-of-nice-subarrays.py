from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        ans = odd_freq = 0
        for num in nums:
            if num % 2 == 1:
                odd_freq += 1
            if odd_freq - k in counts:
                ans += counts[odd_freq - k]
            counts[odd_freq] += 1
        return ans