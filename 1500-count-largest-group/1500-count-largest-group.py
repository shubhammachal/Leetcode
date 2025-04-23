class Solution:
    def countLargestGroup(self, n: int) -> int:
        count = {}

        for i in range(1, n + 1):
            num = i
            dig_sum = 0
            while num > 0:
                dig_sum += num % 10
                num //= 10

            count[dig_sum] = count.get(dig_sum, 0) + 1

        max_size = max(count.values())
        return sum(1 for val in count.values() if val == max_size)
