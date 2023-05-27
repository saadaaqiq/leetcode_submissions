# https://leetcode.com/problems/two-sum-iii-data-structure-design

class TwoSum:

  def __init__(self):
    self.d = {}

  def add(self, n: int) -> None:
    if n not in self.d:
      self.d[n] = 0
    self.d[n] += 1

  def find(self, v: int) -> bool:
    for x in self.d:
      if (v-x == x and self.d[x] > 1) or (v-x != x and v-x in self.d):
        return True
    return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)