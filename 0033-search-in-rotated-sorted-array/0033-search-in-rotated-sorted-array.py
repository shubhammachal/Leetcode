class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid #target found, return mid index
            
            #check which half is sorted
            if nums[left] <= nums[mid]: #if left half is sorted
                if nums[left] <= target < nums[mid]:#check if target is in left half
                    right = mid - 1 #target in left half
                else:
                    left = mid + 1 #target in right half
            
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1



