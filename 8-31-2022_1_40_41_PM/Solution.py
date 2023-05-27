# https://leetcode.com/problems/design-hit-counter

class HitCounter:

  def __init__(self):
    self.arr = []

  def hit(self, timestamp: int) -> None:
    self.arr.append(timestamp)

  def getHits(self, timestamp: int) -> int:
    if len(self.arr) == 0:
      return 0
    l = 0
    r = len(self.arr) - 1
    while l < r:
      mid = (l+r)//2
      if timestamp - self.arr[mid] < 300:
        r = mid
      else:
        l = mid + 1
    c = 0
    if timestamp - self.arr[r] >= 300: 
      c = 1
    return len(self.arr) - r - c

