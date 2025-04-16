from collections import Counter
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counter = Counter() #keep track of current count of number in the window
        pairs = 0
        ans = 0
        l = 0
        for r, num in enumerate(nums):
            pairs += counter[num]
            counter[num] += 1

            while pairs >= k:
                ans += n-r #if we found good subarray at r, the subarray starts
                #at l and ends at r or r+1 or after that is also a good subarray
                counter[nums[l]] -= 1
                pairs -= counter[nums[l]]
                l+= 1
        return ans