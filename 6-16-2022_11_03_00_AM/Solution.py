# https://leetcode.com/problems/paint-house

class Solution:
  def minCost(self, costs: List[List[int]]) -> int:
    tup = (0,0,0)
    for i in range(len(costs)-1, -1, -1):
      tup= (min(costs[i][1]+tup[1],costs[i][2]+tup[2]),min(costs[i][0]+tup[0],costs[i][2]+tup[2]),min(costs[i][0]+tup[0],costs[i][1]+tup[1]))
    return min(tup)