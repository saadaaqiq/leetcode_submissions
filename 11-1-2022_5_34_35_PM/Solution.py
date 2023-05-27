# https://leetcode.com/problems/print-in-order

class Foo:
  def __init__(self):
    self.x = 0


  def first(self, printFirst: 'Callable[[], None]') -> None:
    while self.x != 0:
      continue  
    printFirst()
    self.x = 1


  def second(self, printSecond: 'Callable[[], None]') -> None:
    while self.x != 1:
      continue 
    printSecond()
    self.x = 2


  def third(self, printThird: 'Callable[[], None]') -> None:
    while self.x != 2:
      continue 
    printThird()
    self.x = 0