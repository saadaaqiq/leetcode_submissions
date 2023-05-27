# https://leetcode.com/problems/first-unique-number

class FirstUnique:
  
  def __init__(self, nums: List[int]):
    self.dic, self.notUniques = {}, set()
    for num in nums:
      self.add(num)
        
  def showFirstUnique(self) -> int:
    if not self.dic:
      return -1
    for k in self.dic:
      if k not in self.notUniques:
        return k
    return -1

  def add(self, num: int) -> None:
    if num not in self.notUniques:
      if num in self.dic:
        self.dic.pop(num)
        self.notUniques.add(num)
      else:
        self.dic[num] = None

