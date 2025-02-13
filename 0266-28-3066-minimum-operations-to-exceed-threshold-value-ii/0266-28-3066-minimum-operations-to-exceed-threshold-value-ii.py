import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        operations = 0
        while any(num < k for num in nums) and len(nums) >= 2:
                first = heapq.heappop(nums)
                second = heapq.heappop(nums)
                number = (first * 2) + second
                heapq.heappush(nums, number)
                operations += 1
        return operations


