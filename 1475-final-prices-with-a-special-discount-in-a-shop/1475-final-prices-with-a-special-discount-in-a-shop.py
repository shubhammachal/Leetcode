class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        final_price = prices.copy()
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    final_price[i] = (prices[i] - prices[j])
                    break

        return final_price
    