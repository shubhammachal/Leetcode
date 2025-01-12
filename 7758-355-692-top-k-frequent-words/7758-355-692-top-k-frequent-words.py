from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #we will use hashamp/counter and heap
        #can use min heap and pop till the len(heap) equals k
        #but this won't sort lexiographically
        #so use max heap
        freq = Counter(words)
        heap = []
        res = []
        for key, value in freq.items():
            heapq.heappush(heap, (-value, key))
        
        for i in range(k):
            res.append(heapq.heappop(heap))

        return [pair[1] for pair in res]
