# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        m = prices[0]
        res = 0
        for i in range(1,n):
            res = max(res, prices[i]-m)
            m = min(m, prices[i])
        return res