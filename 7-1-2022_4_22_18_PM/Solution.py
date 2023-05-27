# https://leetcode.com/problems/min-stack

class MinStack:

  def __init__(self):
    self.stack = []
    self.mins = []
    
  def push(self, val: int) -> None:
    self.stack.append(val)
    if not self.mins or val < self.stack[self.mins[-1]]:
      self.mins.append(len(self.stack)-1)

  def pop(self) -> None:
    if self.mins[-1] == len(self.stack)-1:
      self.mins.pop()
    self.stack.pop()
    
  def top(self) -> int:
    return self.stack[len(self.stack)-1]

  def getMin(self) -> int:
    return self.stack[self.mins[-1]]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()