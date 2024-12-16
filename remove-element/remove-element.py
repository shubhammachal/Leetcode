class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums) - 1
        start = 0
        end = n
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
            else:
                start += 1
                
        return start
        