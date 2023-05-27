# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxis = [0] * (n+1)
        for i in range(n-1, -1, -1):
            maxis[i] = max(maxis[i+1], prices[i])
        res = 0
        for i in range(n-1):
            res = max(res, maxis[i+1] - prices[i])
        return res