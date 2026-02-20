class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        r = n -1
        max_coin = 0
        for _ in range(n//3):
            max_coin += piles[r-1]
            r -= 2
        return max_coin
