from collections import defaultdict
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        max_sum = -1
        #idea is to map sum to numbers
        map_sum = defaultdict(list)
        
        for num in nums:
            digits_sum = sum(int(num) for num in str(num))
            map_sum[digits_sum].append(num)

        for value in map_sum.values():
            if len(value) > 1: 
                #we need to get the largest top 2 from the list if more than 2 numbers have the sam e sum
                value.sort(reverse  = True)
                max_sum = max(max_sum, value[0] + value[1])
        return max_sum