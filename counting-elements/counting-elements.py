class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        hash_set = set(arr)
        for num in arr:
            if num + 1 in hash_set:
                count += 1
        return count
                