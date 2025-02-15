class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        #follow up on sum of subarrayminimus
        stack = []
        total_sum = 0
        n = len(nums)
        
        #sum of all the minumums
        for i in range(n + 1):
            while stack and (i == n or nums[stack[-1]] >= nums[i]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                right = i
                count = (mid - left) * (right - mid)
                #subtracted because we have to find diff between maximums and minimum.
                #else store sum of minimums in sep var and max in sep var
                total_sum -= count * nums[mid]
            stack.append(i)

        stack.clear()
        #sum of all maximums
        for i in range(n + 1):
            while stack and (i == n or nums[stack[-1]] <= nums[i]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                right = i
                count = (mid - left) * (right - mid)
                total_sum += count * nums[mid]
            stack.append(i)
        return total_sum
        
