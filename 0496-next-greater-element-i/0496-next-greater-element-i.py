class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums1)
        for i, num1 in enumerate(nums1):
            found = False
            for j, num2 in enumerate(nums2):
                if found and num2 > num1:
                    result[i] = num2
                    break 

                if num2 == num1:
                    found = True
        return result