from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        # keep track of how often certain sum occur.
        
        counts = defaultdict(int) 
        counts[0] = 1
        
        ans = curr = 0
        for num in nums:
            curr += num
            
            #If curr - goal exists in counts, it means there are subarrays ending at the current position where the sum of the subarray equals goal.
            
            if curr - goal in counts: 
                ans += counts[curr-goal] #counts[curr - goal] tells us how many times a prefix sum of curr - goal has been seen.
            counts[curr] += 1
        return ans