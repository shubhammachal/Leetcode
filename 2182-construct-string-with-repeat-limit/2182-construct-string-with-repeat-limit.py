from collections import Counter
import heapq
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = Counter(s)
        result = []
        max_heap = [(-ord(char), count) for char, count in freq.items()]
        heapq.heapify(max_heap)
        
        #step 1
        while max_heap:
            char, count = heapq.heappop(max_heap)
            current_count = min(count, repeatLimit)
            char = chr(-char)
            result.append(char * current_count)
            
            #step 2 basically check for the remaining
            if count - current_count > 0 and max_heap:
                next_char, next_count = heapq.heappop(max_heap)
                next_char = chr(-next_char)
                result.append(next_char)
                
                if next_count > 1:
                    heapq.heappush(max_heap, (-ord(next_char), next_count - 1))
                heapq.heappush(max_heap, (-ord(char), count - current_count))
            
        
        
        return "".join(result)