class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        freq = Counter(nums)

        n = len(nums)
        if n % k != 0:
            return False
        
        for num in sorted(freq.keys()):
            while freq[num] > 0:
                for i in range(k):
                    if freq[num+i] <= 0:
                        return False
                    freq[num + i] -= 1
        return True