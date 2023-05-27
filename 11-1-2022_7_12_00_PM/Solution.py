# https://leetcode.com/problems/print-foobar-alternately

class FooBar:
  def __init__(self, n):
    self.n = n
    self.barrier = threading.Barrier(2)
  
  def foo(self, printFoo: 'Callable[[], None]') -> None:
    for i in range(self.n):
      self.barrier.wait()
      printFoo()
      self.barrier.wait()
      
  def bar(self, printBar: 'Callable[[], None]') -> None:
    for i in range(self.n):
      self.barrier.wait()
      self.barrier.wait()
      printBar()