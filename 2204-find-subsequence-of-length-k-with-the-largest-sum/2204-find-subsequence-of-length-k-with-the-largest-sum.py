import heapq
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []
        result = []
        for index, num in enumerate(nums):
            heapq.heappush(heap, (num, index))
            if len(heap) > k:
                heapq.heappop(heap)
        top_k = list(heap)
        top_k.sort(key = lambda x:x[1])
        return [num for num,index  in top_k]