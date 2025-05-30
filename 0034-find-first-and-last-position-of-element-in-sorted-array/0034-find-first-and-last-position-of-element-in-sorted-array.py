class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
    
        left = 0 
        right = len(nums) - 1
        first_pos = -1
        last_pos = -1
        #for first position
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                first_pos = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            
        #for last position
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                last_pos = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return [first_pos, last_pos]
