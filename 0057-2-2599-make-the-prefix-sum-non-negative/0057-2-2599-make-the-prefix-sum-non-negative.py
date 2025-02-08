import heapq
class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        count = 0
        prefix = 0
        min_heap = []
        for num in nums:
            prefix += num
            if num < 0:
                heapq.heappush(min_heap, num)
        
            while min_heap and prefix < 0:
                prefix -= heapq.heappop(min_heap)
                count += 1
        return count

