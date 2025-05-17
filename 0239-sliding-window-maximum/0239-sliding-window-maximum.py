class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        res = []
        heap = []
        for right in range(len(nums)):
            heapq.heappush(heap, (-nums[right], right))

            if right >= k - 1:
                while heap[0][1] <= right - k:
                    heapq.heappop(heap)
                res.append(-heap[0][0])
        return res
