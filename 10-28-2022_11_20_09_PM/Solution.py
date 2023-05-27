# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    arr1 = [0]*len(prices)
    arr2 = [0]*len(prices)
    maxRight = -float("infinity")
    for i in range(len(prices)-1, -1, -1):
      maxRight = max(maxRight, prices[i])
      arr1[i] = maxRight
    minLeft = float("infinity")
    for i in range(len(prices)):
      minLeft = min(minLeft, prices[i])
      arr2[i] = minLeft
    return max([arr1[i]-arr2[i] for i in range(len(prices))])