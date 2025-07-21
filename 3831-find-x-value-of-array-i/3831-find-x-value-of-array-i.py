from collections import defaultdict
class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        res = [0] * k
        dp = defaultdict(int)
        for num in nums:
            new_dp = defaultdict(int)
            mod = num % k
            new_dp[mod] += 1

            for prev_mod in dp:
                new_mod = (prev_mod * num) % k
                new_dp[new_mod] += dp[prev_mod]

            for rem in new_dp:
                res[rem] += new_dp[rem]
            dp = new_dp
        return res
        