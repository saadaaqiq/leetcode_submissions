# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    m = 0
    maxProfit = 0
    for i in range(len(prices)-1, -1, -1):
      m = max(m, prices[i])
      maxProfit = max(maxProfit, m - prices[i])
    return maxProfit