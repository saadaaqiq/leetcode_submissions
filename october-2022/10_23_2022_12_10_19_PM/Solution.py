# https://leetcode.com/problems/logger-rate-limiter

class Logger:

  def __init__(self):
    self.dic = {}

  def shouldPrintMessage(self, t: int, m: str) -> bool:
    if m in self.dic:
      if t >= self.dic[m]:
        self.dic[m] = t + 10
        return True
      else:
        return False
    else:
      self.dic[m] = t + 10
      return True
      
    


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)