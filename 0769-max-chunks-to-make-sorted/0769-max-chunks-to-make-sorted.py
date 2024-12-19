class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        prefix_max = arr[:]
        suffix_min = arr[:]

        for i in range(1, len(arr)):
            prefix_max[i] = max(prefix_max[i-1],prefix_max[i])
        
        for i in range(len(arr) - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i], suffix_min[i+1])

        chunks = 0

        for i in range(len(arr)):
            if i == 0 or suffix_min[i] > prefix_max[i - 1]:
                chunks += 1
        return chunks
