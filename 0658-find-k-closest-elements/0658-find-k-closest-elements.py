import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for num in arr:
            diff = abs(x - num)
            heapq.heappush(heap, (-diff, -num))
            
        while len(heap) > k:
            heapq.heappop(heap)
            
        return sorted([-pair[1] for pair in heap])