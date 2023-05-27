# https://leetcode.com/problems/zigzag-iterator

class ZigzagIterator:
  def __init__(self, v1: List[int], v2: List[int]):
    self.it = heapq.merge([[i,x] for (i,x) in enumerate(v1)], [[j,y] for (j,y) in enumerate(v2)], key=lambda x: x[0])
    self.l = len(v1) + len(v2)
    self.c = 0 

  def next(self) -> int:
    self.c += 1
    if self.c <= self.l:
      return self.it.__next__()[1]

  def hasNext(self) -> bool:
    return self.c < self.l

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())