# https://leetcode.com/problems/online-stock-span

class StockSpanner:
  def __init__(self):
    self.values = []
    self.span = []

  def next(self, price: int) -> int:
    sp = 1
    i = len(self.values)-1
    while i >= 0 and self.values[i] <= price:
      sp += self.span[i]
      i -= self.span[i]
    self.values.append(price)
    self.span.append(sp)
    return sp