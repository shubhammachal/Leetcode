class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        if len(set(nums)) == 1:
            return "equilateral"
        elif len(set(nums)) == 3:
            return "scalene"
        else:
            return "isosceles"
            

