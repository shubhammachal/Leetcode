class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        #brute force
        
        elem_counted = 1
        nums.sort(reverse = True)
        
        prev_elem = nums[0]
        
        for i in range(1,len(nums)):
            
            if nums[i] != prev_elem:
                elem_counted += 1
                prev_elem = nums[i]
                
            if elem_counted == 3:
                return nums[i]
        return nums[0]
                
        