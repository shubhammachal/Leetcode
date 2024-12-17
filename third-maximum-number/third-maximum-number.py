import heapq
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        min_heap = []
        seen = set()

        for num in nums:
            if num not in seen:
                seen.add(num)
                heapq.heappush(min_heap, num)

                if len(min_heap) > 3:
                    heapq.heappop(min_heap)
        if len(min_heap) < 3:
            return max(min_heap)
        return min_heap[0]