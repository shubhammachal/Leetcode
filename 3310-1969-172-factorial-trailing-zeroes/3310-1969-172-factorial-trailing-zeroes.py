class Solution:
    def trailingZeroes(self, n: int) -> int:
        zero_count = 0
        for i in range(5, n+1, 5):
            rem_i = i
            while rem_i % 5 == 0:
                zero_count += 1
                rem_i //= 5
        return zero_count

        