import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(math.sqrt(c))
        while left <= right:
            sum_of_sq = left * left + right * right
            if sum_of_sq == c:
                return True
            elif sum_of_sq < c:
                left += 1
            else:
                right -= 1
        return False
