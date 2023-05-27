# https://leetcode.com/problems/gas-station

class Solution:
  def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    if sum(gas) < sum(cost): 
      return -1
    i, j, s = 0, 0, 0
    while i < len(gas) and j < len(gas):
      s += gas[j] - cost[j]
      if s < 0:
        i = j + 1
        j = i
        s = 0
      else:
        j += 1

    return i if s >= 0 else -1
        
    