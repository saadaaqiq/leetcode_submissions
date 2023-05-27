# https://leetcode.com/problems/daily-temperatures

class Solution:
  def dailyTemperatures(self, temps: List[int]) -> List[int]:
    stack = [(temps[-1], len(temps)-1)]
    res = [0] * len(temps)
    
    if len(temps)>1:
      for i in range(len(temps)-2, -1, -1):
        if temps[i] >= stack[-1][0]:
          while stack and temps[i] >= stack[-1][0]:
            stack.pop()
          if not stack:
            res[i] = 0
          else:
            res[i] = stack[-1][1] - i
          stack.append((temps[i],i))
        else:
          res[i] = 1
          stack.append((temps[i],i))
    
    return res