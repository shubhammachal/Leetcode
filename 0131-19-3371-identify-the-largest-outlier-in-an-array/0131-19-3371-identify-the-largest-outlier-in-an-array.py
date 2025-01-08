from collections import defaultdict
class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        
        total_sum = sum(nums)
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        max_outlier = float('-inf')

        for num in nums:
            required_sum = total_sum - num
            if required_sum % 2 != 0:
                continue

            potential_sum = required_sum // 2
            freq_map[num] -= 1
            count = freq_map[potential_sum] if potential_sum in freq_map else 0

            if count > 0:
                max_outlier = max(max_outlier, num)

            freq_map[num] += 1

        return max_outlier


