class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        prefix_sum = sorted_prefix_sum = 0
        sorted_arr = sorted(arr)
        chunks = 0
        
        for i in range(len(arr)):
            prefix_sum += arr[i]
            sorted_prefix_sum += sorted_arr[i]
            
            if prefix_sum == sorted_prefix_sum:
                chunks += 1
                
        
        return chunks
