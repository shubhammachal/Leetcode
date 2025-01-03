class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hash_map = {}
        sums = 0
        for num in nums:
            hash_map[num] = hash_map.get(num, 0 ) + 1
        for num, value in hash_map.items():
            if value < 2:
                sums += num
        return sums