# https://leetcode.com/problems/maximum-distance-in-arrays

class Solution:
  def maxDistance(self, arrays: List[List[int]]) -> int:
    
    a, aa, ma, b, bb, mb = 10001, 10001, -1, -10001, -10001, -1
    
    for i, arr in enumerate(arrays):
      if arrays[i][0] < a:
        aa = a
        a = arrays[i][0]
        ma = i
      elif arrays[i][0] <= aa:
        aa = arrays[i][0]
      if arrays[i][-1] > b:
        bb = b
        b = arrays[i][-1]
        mb = i
      elif arrays[i][-1] > bb:
        bb = arrays[i][-1]
    
    if ma != mb:
      return abs(a-b)
    return max(abs(a-bb), abs(aa-b))
