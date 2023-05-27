# https://leetcode.com/problems/insert-delete-getrandom-o1

class RandomizedSet:
  def __init__(self):
    self.A = {}
    self.B = {}
    self.size = 0

  def insert(self, v: int) -> bool:
    if v in self.A:
      return False
    else:
      self.A[v] = self.size
      self.B[self.size] = v
      self.size += 1
      return True

  def remove(self, v: int) -> bool:
    if v not in self.A:
      return False
    else:
      temp = self.A[v]
      self.A.pop(v)
      if temp != self.size - 1:
        self.A[self.B[self.size-1]] = temp
        self.B[temp] = self.B[self.size-1]
      self.B.pop(self.size-1)
      self.size -= 1
      return True

  def getRandom(self) -> int:
    r = random.randint(0,self.size-1)
    
    return self.B[r]
