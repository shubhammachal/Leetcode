class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        j_index = []
        n = len(nums)
        res = set()
        for i in range(n):
            for j in range(n):
                if nums[j] == key and abs(i-j) <= k:
                    res.add(i)
                    break
        return sorted(res)