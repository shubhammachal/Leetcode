class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        arr = [(value,index) for index, value in enumerate(nums)]
        arr.sort(key = lambda x:x[0])
        
        #minimize index and maximize width
        min_index_so_far = float('inf')
        max_width = 0
        
        for value, index in arr:
            if index > min_index_so_far:
                max_width = max(max_width, index - min_index_so_far)
            min_index_so_far = min(index, min_index_so_far)
            
        return max_width
                