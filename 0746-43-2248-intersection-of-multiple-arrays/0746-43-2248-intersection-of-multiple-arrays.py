from collections import defaultdict
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        res = []
        count = defaultdict(int)
        for arr in nums:
            for num in arr:
                count[num] += 1
        for key in count:
            if count[key] == n:
                res.append(key)
        return sorted(res)