# https://leetcode.com/problems/daily-temperatures

class Solution:
  def dailyTemperatures(self, temps: List[int]) -> List[int]:
    stack = [len(temps)-1]
    res = [0] * len(temps)
    
    if len(temps)>1:
      for i in range(len(temps)-2, -1, -1):
        if temps[i] >= temps[stack[-1]]:
          while stack and temps[i] >= temps[stack[-1]]:
            stack.pop()
          if not stack:
            res[i] = 0
          else:
            res[i] = stack[-1] - i
        else:
          res[i] = 1
        stack.append(i)
    
    return res