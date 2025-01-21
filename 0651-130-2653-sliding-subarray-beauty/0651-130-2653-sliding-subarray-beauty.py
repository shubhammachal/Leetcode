from sortedcontainers import SortedList
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        #we can use sortedlist, maintain a rolling window of sorted values
        #used in problems where a sliding window needs to be sorted dynamically.
        n = len(nums)
        result = []
        negatives = SortedList()
        for i in range(n):
            if nums[i] < 0:
                negatives.add(nums[i])
            if i >= k and nums[i - k ] < 0:
                negatives.remove(nums[i-k])
            if i >= k - 1:
                if len(negatives) >= x:
                    result.append(negatives[x - 1])
                else:
                    result.append(0)
        return result