from collections import Counter
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        z1 = z2 = 0
        sum1 = sum2 = 0
        for num in nums1:
            sum1 += num
            if num == 0:
                sum1 += 1
                z1 += 1
        for num in nums2:
            sum2 += num
            if num == 0:
                z2 += 1
                sum2 += 1
        if (sum1 > sum2 and z2 == 0) or (sum2 > sum1 and z1 == 0):
            return -1
        return max(sum1, sum2)