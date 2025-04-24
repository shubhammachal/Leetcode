class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        number_of_distinct = len(set(nums))
        count = 0
        n = len(nums)
        for i in range(n):
            unique = set()
            for j in range(i,n):
                unique.add(nums[j])
                if len(unique) == number_of_distinct:
                    count += n - j
                    break
        return count
