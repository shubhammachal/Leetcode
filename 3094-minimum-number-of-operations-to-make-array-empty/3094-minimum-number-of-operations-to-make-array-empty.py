class Solution:
    def minOperations(self, nums: List[int]) -> int:
        min_op = 0
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1
        
        for val in count.values():
            if val == 1:
                return - 1
            
            min_op += ceil(val/3)
        return min_op

