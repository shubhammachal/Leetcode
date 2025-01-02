class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        # Edge case: return -1 if the input list is empty
        if not nums:
            return -1
        
        # Count occurrences of each number
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        # Find the largest number with exactly one occurrence
        largest = -1
        for num, count in frequency.items():
            if count == 1:
                largest = max(largest, num)
        
        return largest
