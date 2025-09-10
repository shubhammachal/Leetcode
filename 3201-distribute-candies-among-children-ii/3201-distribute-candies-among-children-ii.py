class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        total_ways = 0

            #first kid i
            # second j >= 0
            # j <= limit
            # i + j <= n
            #3rd child gets n - i - j so 0 <= n - i - j <= limit
            # n - i - limit <= j <= n - i
         #If the other two children get maximum limit candies each, the first child must get at least n - 2 * limit candies
        start = max(0, n - 2 * limit)
        end = min(n, limit)
        for i in range(start, end+ 1):

            j_min = max(0, n - i -limit)
            j_max = min(limit, n - i)

            if j_max >= j_min:
                ways_for_this_i = j_max - j_min + 1
                total_ways += ways_for_this_i
        return total_ways
