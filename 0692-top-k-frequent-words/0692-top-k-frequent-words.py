import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq_count = {}
        for word in words:
            freq_count[word] = freq_count.get(word, 0) + 1
        heap = []
        for word, freq in freq_count.items():
            heapq.heappush(heap, (-freq,word))
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap))
        
        return [pair[1] for pair in res]
        
            