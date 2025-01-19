class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digits = [int(d) for d in str(n)]
        n = len(digits)
        res = 0
        sign = 1
        for i in range(n):
            if i % 2 == 0:
                res += sign * digits[i]
            else:
                res += -sign * digits[i]
        return res