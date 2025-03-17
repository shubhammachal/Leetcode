from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        return all(value % 2 == 0 for value in freq.values())