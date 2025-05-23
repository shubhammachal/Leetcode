class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        max_profit = 0
        while(right < len(nums)):
            if prices[right] > prices[left]:
                current_profit = prices[right] - prices[left]
                max_profit = max(current_profit, max_profit)

            else:
                left = right
            right += 1
        return max_profit
