"""optimal solution using kadane's algorithm
brute force is O(N^3) and can be optimized to O(N^2).
Time complexity of this approach is O(N) and space complexity is O(1)"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        curr_sum = 0
    
        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num
                
            if curr_sum > max_sum:
                max_sum = curr_sum
        return max_sum