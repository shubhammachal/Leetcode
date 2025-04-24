class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        number_of_distinct = len(set(nums))
        count = 0
        for i in range(len(nums)):
            unique = set()
            for j in range(i,len(nums)):
                unique.add(nums[j])
                if len(unique) == number_of_distinct:
                    count += 1
        return count
