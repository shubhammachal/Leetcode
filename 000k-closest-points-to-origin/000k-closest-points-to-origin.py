import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for x, y in points:
            sq_dist =  -(x**2 + y**2)
            heapq.heappush(heap, (sq_dist, [x,y]))
        
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [point for _, point in heap]