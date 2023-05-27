# https://leetcode.com/problems/moving-average-from-data-stream

class MovingAverage:

  def __init__(self, size: int):
    self.q = deque()
    self.size = size
    self.c = 0
    self.old = 0

  def next(self, x: int) -> float:
    self.q.append(x)
    if self.c < self.size:
      self.c += 1
      self.old = self.old*(self.c-1)/self.c + x/self.c
    else:
      cache = self.q.popleft()
      self.old = self.old - cache/self.size + x/self.size
    return self.old

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)