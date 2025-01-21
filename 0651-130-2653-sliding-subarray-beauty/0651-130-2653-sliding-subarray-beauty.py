from sortedcontainers import SortedList
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        #we can use sortedlist, maintain a rolling window of sorted values
        #used in problems where a sliding window needs to be sorted dynamically.
        n = len(nums)
        result = []
        negatives = SortedList()
        #only add negatives to negatives list, it will store negative numbers in sorted order
        for i in range(n):
            if nums[i] < 0:
                negatives.add(nums[i])
            #check for window size: if it is greater than k, remove the leftmost
            if i >= k and nums[i - k ] < 0:
                negatives.remove(nums[i-k])
            
            #if window size == k - 1, start appending to result
            #if k = 3, first full window will be at index 2(3-1)
            if i >= k - 1:
                if len(negatives) >= x:
                    #since negatives is a sorted list, x-1 will be the xth smallest negative element
                    result.append(negatives[x - 1])
                else:
                    result.append(0)
        return result