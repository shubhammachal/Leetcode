class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            if nums[i] < pivot:
                result.append(nums[i])
        for i in range(len(nums) ):
            if nums[i] == pivot:
                result.append(nums[i])
        for i in range(len(nums) ):
            if nums[i] > pivot:
                result.append(nums[i])
        return result