class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hash_set = set(nums)
        n = len(nums)
        res = []
        for i in range(1, n+1):
            if i not in hash_set:
                res.append(i)
        return res