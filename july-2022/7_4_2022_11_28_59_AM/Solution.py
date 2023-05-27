# https://leetcode.com/problems/min-stack

class MinStack:

  def __init__(self):
    self.stack = []
    self.mins = []
    self.head = -1
    self.min = -1
    
  def push(self, val: int) -> None:

    self.head += 1
    if self.head == len(self.stack):
      self.stack.append(val)
    else:
      self.stack[self.head] = val
    if not self.mins:
      self.min += 1
      self.mins.append(self.head)
    else:
      if val <= self.stack[self.mins[self.min]]:
        self.min += 1
        if self.min == len(self.mins):
          self.mins.append(self.head)
        else:
          self.mins[self.min] = self.head
    
  def pop(self) -> None:
    if self.mins[self.min] == self.head:
      self.min -= 1
    self.head -= 1
    if self.min == -1:
      self.mins.clear()
    if self.head == -1:
      self.stack.clear()
    
  def top(self) -> int:
    return self.stack[self.head]

  def getMin(self) -> int:
    return self.stack[self.mins[self.min]]

