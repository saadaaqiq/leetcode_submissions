# https://leetcode.com/problems/daily-temperatures

class Solution:
  def dailyTemperatures(self, temps: List[int]) -> List[int]:
    stack = [len(temps)-1]
    res = [0] * len(temps)
    
    i = len(temps) - 2
    while i >= 0:
      while stack and temps[i] >= temps[stack[-1]]:
        stack.pop()
      if not stack:
        res[i] = 0
      else:
        res[i] = stack[-1] - i
      stack.append(i)
      i -= 1
    
    return res