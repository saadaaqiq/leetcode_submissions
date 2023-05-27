# https://leetcode.com/problems/maximum-units-on-a-truck

class Solution:
  def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
    boxTypes.sort(key=lambda x:x[1], reverse=True)
    res = 0
    bInTruck = 0
    for nOfBoxes, unitsPerBox in boxTypes:
      j = 0
      while bInTruck < truckSize and j < nOfBoxes:
        res += unitsPerBox
        bInTruck += 1
        j += 1
      if bInTruck == truckSize:
        return res
    return res