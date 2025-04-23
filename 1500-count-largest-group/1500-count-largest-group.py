class Solution:
    def countLargestGroup(self, n: int) -> int:
        count = {}
        if n == 0:
            return 0
        for i in range(1, n + 1):
            dig_sum = sum(int(d) for d in str(i))
            count[dig_sum] = count.get(dig_sum, 0 ) + 1
        max_size = max(count.values())

        ans = 0
        for val in count.values():
            if val == max_size:
                ans += 1
        return ans
