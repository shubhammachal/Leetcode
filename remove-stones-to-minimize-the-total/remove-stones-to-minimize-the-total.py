import heapq
import math
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        heap = [-pile for pile in piles]
        heapq.heapify(heap)
        while k:
            largest = - heapq.heappop(heap)
            reduced = math.ceil(largest / 2)
            heapq.heappush(heap, -reduced)
            k -= 1
        return -sum(heap)
        
        
        