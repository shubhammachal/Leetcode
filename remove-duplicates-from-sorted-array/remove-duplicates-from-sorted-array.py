class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_count = 1

        # Iterate through the sorted list and update it in-place
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[unique_count] = nums[i]
                unique_count += 1

        # Return the length of the modified list
        return unique_count