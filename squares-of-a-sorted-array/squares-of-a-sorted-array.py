class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        head = 0
        n = len(nums)
        tail = n-1
        res = [0] * n
        nums = [num ** 2 for num in nums]
        
        for i in range(n-1, -1, -1):
            if nums[head] < nums[tail]:
                res[i] = nums[tail]
                tail -= 1
            else:
                res[i] = nums[head]
                head += 1
        return res