# https://leetcode.com/problems/zigzag-iterator

class ZigzagIterator:
  def __init__(self, v1: List[int], v2: List[int]):
    self.q = deque()
    queues = [deque(v1), deque(v2)]
    i = 0
    while queues[0] or queues[1]:
      if queues[i]:
        self.q.append(queues[i].popleft())
      i += 1 
      if i == len(queues):
        i = 0
    
    

  def next(self) -> int:
    return self.q.popleft()

  def hasNext(self) -> bool:
    return bool(self.q)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())