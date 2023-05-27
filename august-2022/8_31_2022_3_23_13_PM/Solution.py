# https://leetcode.com/problems/design-hit-counter

class HitCounter:

  def __init__(self):
    self.arr = []
    self.start = 0

  def hit(self, timestamp: int) -> None:
    self.arr.append(timestamp)    
    l, r = self.start, len(self.arr) - 1
    while l < r:
      mid = (l+r)//2
      (r,l) = (mid,l) if timestamp - self.arr[mid] < 300 else (r,mid + 1)
    self.start = r-1 if timestamp - self.arr[r] >= 300 else r
    
  def getHits(self, timestamp: int) -> int:
    self.hit(timestamp)
    self.arr.pop()
    return len(self.arr) - self.start
    
    