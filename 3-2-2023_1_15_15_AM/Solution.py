# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr = prices.copy()
        for i in range(len(prices)-2, -1, -1):
            arr[i] = max(arr[i], arr[i+1])
        m = math.inf
        res = -math.inf
        for i in range(len(prices)):
            m = min(prices[i], m)
            res = max(res, arr[i] - m)
        return res