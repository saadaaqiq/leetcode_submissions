# https://leetcode.com/problems/gas-station

class Solution:
  def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    if sum(gas) < sum(cost): 
      return -1
    remainder = [gas[i] - cost[i] for i in range(len(gas))]
    i, j, s = 0, 0, 0
    while i < len(remainder) and j < len(remainder):
      s += remainder[j]
      if s < 0:
        i = j + 1
        j = i
        s = 0
      else:
        j += 1

    return i if s >= 0 else -1
        
    