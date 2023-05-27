# https://leetcode.com/problems/maximum-distance-in-arrays

class Solution:
  def maxDistance(self, arrays: List[List[int]]) -> int:
    maxi, maxipos = max([(arr[-1], i) for (i, arr) in enumerate(arrays)], key=lambda x: x[0])
    mini, minipos = min([(arr[0], i) for (i, arr) in enumerate(arrays)], key=lambda x: x[0])
    if maxipos!=minipos:
      return abs(maxi-mini)
    secondmaxi, secondmaxipos = max([(arr[-1], i) for (i, arr) in enumerate(arrays) if i!=maxipos], key=lambda x: x[0])
    secondmini, secondminipos = min([(arr[0], i) for (i, arr) in enumerate(arrays) if i!=minipos], key=lambda x: x[0])
    if maxipos != secondminipos and secondmaxipos != minipos:
      return max(abs(maxi-secondmini), abs(secondmaxi-mini))
    if secondmaxipos != secondminipos:
      return abs(secondmaxi-secondmini)
    return 0