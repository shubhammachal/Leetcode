class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        hm = {}
        res = []
        temp = sorted(nums)
        for index, val in enumerate(temp):
            if val not in hm:
                hm[val] = index
        for num in nums:
            res.append(hm[num])
        return res