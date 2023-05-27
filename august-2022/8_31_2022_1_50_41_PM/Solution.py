# https://leetcode.com/problems/design-hit-counter

class HitCounter:

  def __init__(self):
    self.q = deque()

  def hit(self, timestamp: int) -> None:
    self.q.append(timestamp)
    while self.q and timestamp - self.q[0] >= 300:
      self.q.popleft()

  def getHits(self, timestamp: int) -> int:
    while self.q and timestamp - self.q[0] >= 300:
      self.q.popleft()
    return len(self.q)

