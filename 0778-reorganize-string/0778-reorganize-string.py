import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = []
        count_map = Counter(s)
        heap = [(-freq, char) for char, freq in count_map.items()]
        heapq.heapify(heap)

        while heap:
            first_count, first_char = heapq.heappop(heap)
            if not ans or first_char != ans[-1]:  # Ensure no consecutive chars
                ans.append(first_char)
                first_count += 1  # Increment (because it's negative)
                if first_count != 0:  # Only push if there are more occurrences
                    heapq.heappush(heap, (first_count, first_char))
            else:
                if not heap:  # No valid character to place
                    return ""
                second_count, second_char = heapq.heappop(heap)
                ans.append(second_char)
                second_count += 1
                if second_count != 0:
                    heapq.heappush(heap, (second_count, second_char))
                heapq.heappush(heap, (first_count, first_char))  # Push first back

        return "".join(ans)