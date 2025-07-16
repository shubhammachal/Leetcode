class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        number_of_ways = 0
        for a in range(limit+1):
            for b in range(limit+1):
                c = n - (a + b)
                if 0 <= c <= limit and a + b + c == n:
                    number_of_ways += 1
                
        return number_of_ways