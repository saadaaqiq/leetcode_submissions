# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    arr1 = [0]*len(prices) + [-1]
    arr2 = [100001] + [0]*len(prices)
    for i in range(len(prices)-1,-1,-1):
      arr1[i] = max(arr1[i+1], prices[i])
    for i in range(len(prices)):
      arr2[i+1] = min(arr2[i], prices[i])
    return max([arr1[i]-arr2[i+1] for i in range(len(prices))])
  