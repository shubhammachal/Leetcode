import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        heap = [-f for f in freq if f > 0]
        heapq.heapify(heap)
        
        time = 0
        while heap:
            cycle = n + 1
            store = []
            task_count = 0
            while cycle > 0 and heap:
                current_freq = -heapq.heappop(heap)
                if current_freq > 1:
                    store.append(-(current_freq - 1))
                task_count += 1
                cycle -= 1
            for x in store:
                heapq.heappush(heap, x)
            time += task_count if not heap else n + 1
        return time
