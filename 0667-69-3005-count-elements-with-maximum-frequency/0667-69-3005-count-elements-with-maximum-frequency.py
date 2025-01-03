from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = Counter(nums)
        maximum = max(counts.values())
        ans = 0
        for value in counts.values():
            if value == maximum:
                ans += value
        return ans