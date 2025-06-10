import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(mid):
            #number of hours needed to finish all the bananas
            return sum(math.ceil(pile/mid) for pile in piles)

        left = 1
        right = max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if hours_needed(mid) > h:
                left = mid + 1
            elif hours_needed(mid) <= h:
                right = mid
        return left

        