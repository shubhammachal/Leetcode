from collections import Counter
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counter = Counter()
        pairs = 0
        ans = 0
        l = 0
        for r, num in enumerate(nums):
            pairs += counter[num]
            counter[num] += 1

            while pairs >= k:
                ans += n-r
                counter[nums[l]] -= 1
                pairs -= counter[nums[l]]
                l+= 1
        return ans