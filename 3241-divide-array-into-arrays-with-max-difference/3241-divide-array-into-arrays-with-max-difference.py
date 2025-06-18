class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        sorted_nums = sorted(nums)
        result = []
        for i in range(0,len(sorted_nums) - 2, 3):
            print(i)
            if sorted_nums[i+2] - sorted_nums[i] > k:
                return []
            else:
                result.append(sorted_nums[i:i+3])
        return result