class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0 ) + 1
        largest = -1
        for key, values in counts.items():
            if counts[key] < 2:
                largest = max(largest, key)
        return largest
                
        