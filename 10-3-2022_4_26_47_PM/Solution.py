# https://leetcode.com/problems/minimum-time-to-make-rope-colorful

class Solution:
  def minCost(self, colors: str, time: List[int]) -> int:
    i = 0
    res = 0
    while i < len(colors)-1:
      if colors[i] == colors[i+1]:
        if time[i] <= time[i+1]:
          res += time[i]
        else:
          res += time[i+1]
          time[i+1] = time[i]
      i += 1
    return res