# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop

class Solution:
  def finalPrices(self, prices: List[int]) -> List[int]:
    monotonic = []
    for j in range(len(prices)):
      while monotonic and prices[j] <= monotonic[-1][0]:
        discount, ind = monotonic.pop()
        prices[ind] -= prices[j]
      monotonic.append((prices[j],j))
    return prices