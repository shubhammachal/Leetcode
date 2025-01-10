class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        #sliding window, two contraints: size of the window is k and no duplicate
        # for no duplicates, use a hashset
        seen = set()
        left = 0
        curr_sum = max_sum = 0
        for right in range(len(nums)):
            while nums[right] in seen or right - left >= k:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1
            curr_sum += nums[right]
            seen.add(nums[right])
            #only update the max sum if window size is k
            if right - left + 1 >= k:
                max_sum = max(max_sum, curr_sum)
        return max_sum