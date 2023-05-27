# https://leetcode.com/problems/zigzag-iterator

class ZigzagIterator:
  def __init__(self, v1: List[int], v2: List[int]):
    self.v1, self.v2 = v1, v2
    self.i, self.j = 0, 0
    self.isI = True if len(v1) > 0 else False

  def next(self) -> int:
    if (self.isI and self.i < len(self.v1)):
      if self.j < len(self.v2):
        self.isI = False
      self.i += 1
      return self.v1[self.i-1]
    if (not self.isI and self.j < len(self.v2)):
      if self.i < len(self.v1):
        self.isI = True
      self.j += 1
      return self.v2[self.j-1]
    return -1

  def hasNext(self) -> bool:
    if (self.isI and self.i < len(self.v1)) or (not self.isI and self.j < len(self.v2)):
      return True
    else:
      return False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())