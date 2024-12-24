class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        smallest = float('inf')
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                smallest = min(smallest, nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return smallest if smallest != float('inf') else -1
                
                