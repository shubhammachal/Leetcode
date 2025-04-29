class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maximum = max(nums)
        n = len(nums)
        max_count = 0
        res = 0
        left = 0
        for right in range(n):
            if nums[right] == maximum:
                max_count += 1

                while max_count >= k:
                    res += (n-right)
                    if nums[left] == maximum:
                        max_count -= 1
                    left += 1
        return res
    

