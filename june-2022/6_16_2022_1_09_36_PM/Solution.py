# https://leetcode.com/problems/paint-house-ii

class Solution:
  def minCostII(self, costs: List[List[int]]) -> int:
    tup = [0] * len(costs[0])
    for i in range(len(costs)-1, -1, -1):
      xtup = []
      for j in range(len(costs[0])):
        l = [ costs[i][p] + tup[p] for p in range(len(costs[0])) if p != j ]
        xtup.append(min(l))
      tup = xtup
    return min(tup)