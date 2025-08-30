import math
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return (math.floor(n/2) * math.ceil(m/2)) + (math.floor(m/2) * math.ceil(n/2))