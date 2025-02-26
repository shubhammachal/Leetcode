class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        is_negative = num < 0
        num = abs(num)
        res = ""
        while num:
            res = str(num % 7) + res
            num //= 7
        return "-" + res if is_negative else res
            