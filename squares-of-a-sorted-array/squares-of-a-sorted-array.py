class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        nums = [num ** 2 for num in nums]
        
        head = 0
        tail = len(nums) - 1
        
        for i in range(len(nums)-1, -1, -1):
            if nums[head] < nums[tail]:
                res[i] = nums[tail]
                tail -= 1
            else:
                res[i] = nums[head]
                head += 1
        return res
        