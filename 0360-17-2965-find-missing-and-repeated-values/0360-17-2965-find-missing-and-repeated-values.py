class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        freq = {}
        for row in grid:
            for element in row:
                freq[element] = freq.get(element, 0) + 1
        for num in range(1, n * n + 1):
            if num not in freq:
                missing = num
            elif freq[num] > 1:
                duplicate = num
        return [duplicate, missing]