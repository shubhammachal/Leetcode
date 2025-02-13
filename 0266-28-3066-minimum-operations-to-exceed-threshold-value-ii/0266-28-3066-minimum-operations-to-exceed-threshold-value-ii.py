import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if len(nums) < 2: 
            return 0
        
        
        heapq.heapify(nums)
        operations = 0
        while nums[0] < k and len(nums) >= 2:
                first = heapq.heappop(nums)
                second = heapq.heappop(nums)
                number = (first * 2) + second
                heapq.heappush(nums, number)
                operations += 1
        return operations


