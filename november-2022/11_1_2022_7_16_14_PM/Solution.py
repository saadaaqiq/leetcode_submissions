# https://leetcode.com/problems/print-foobar-alternately

class FooBar:
  def __init__(self, n):
    self.n = n
    self.fooL = threading.Lock()
    self.barL = threading.Lock()
    self.barL.acquire()
    
  def foo(self, printFoo: 'Callable[[], None]') -> None:
    for i in range(self.n):
      self.fooL.acquire()
      try:
        printFoo()
      finally:
        self.barL.release()
      
  def bar(self, printBar: 'Callable[[], None]') -> None:
    for i in range(self.n):
      self.barL.acquire()
      try:
        printBar()
      finally:
        self.fooL.release()