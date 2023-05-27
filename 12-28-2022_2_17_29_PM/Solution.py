# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        sold, hold, reset  = -math.inf, -math.inf, 0
        for price in prices:
            sold, reset, hold = price + hold, max(sold, reset), max(hold, reset-price)
        return max(sold, reset)





