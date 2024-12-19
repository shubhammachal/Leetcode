import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        heap = []
        
        for num, freq in hm.items():
            heapq.heappush(heap, (freq, num))
            
            if len(heap) > k:
                heapq.heappop(heap)
                
        return [num[1] for num in heap]