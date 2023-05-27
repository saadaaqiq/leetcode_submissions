# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    if len(prices)==1:
        return 0
    mins = [0]*len(prices)
    maxes = [0]*len(prices)
    for i in range(len(prices)):
        mins[i] = prices[i] if i==0 else min(prices[i], mins[i-1])
    for i in range(len(prices)-1, -1, -1):
        maxes[i] = prices[-1] if i == len(prices)-1 else max(prices[i], maxes[i+1])
    return max([maxes[i]-mins[i] for i in range(len(prices))])