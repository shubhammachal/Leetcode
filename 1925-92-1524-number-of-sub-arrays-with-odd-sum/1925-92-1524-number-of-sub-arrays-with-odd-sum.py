class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = (10**9) + 7
        prefix_sum = 0
        even_count = 1
        odd_count = 0
        ans = 0
        for num in arr:
            prefix_sum += num
            parity = prefix_sum % 2
            if parity:
                ans += even_count
                odd_count += 1
            if not parity:
                ans += odd_count
                even_count += 1
        return int(ans % mod)






        