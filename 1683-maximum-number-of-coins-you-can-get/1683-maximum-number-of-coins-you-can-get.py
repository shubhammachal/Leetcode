class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        print(piles)
        n = len(piles)
        coins = 0
        for i in range(int(n/3), n, 2):
            coins += piles[i]
        return coins
