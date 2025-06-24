class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        j_index = []
        n = len(nums)
        res = set()
        for index in range(n):
            if nums[index] == key:
                j_index.append(index)
        for j in j_index:
            for i in range(max(0, j - k), min(n, j + k + 1)):
                
                    res.add(i)
        return sorted(res)
