from collections import defaultdict
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        freq_map = defaultdict(int)
        good_pairs = 0
        total_pairs = (n * (n-1))//2
        for i, num in enumerate(nums):
            diff = num - i
            good_pairs += freq_map[diff]
            freq_map[diff] += 1

        return total_pairs - good_pairs