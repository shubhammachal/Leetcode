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
    
    #time complexity: for hashmap it is O(n)
    # and for heap for every push/pop is O(logk) 
    # and do for every unique element O(mlogk), no of unique elements = m
    # total complexity O(n + m log k), m always less than n so 
    # O(nlogk)