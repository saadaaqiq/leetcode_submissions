# https://leetcode.com/problems/3sum

class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    res = []
    dic = { -x: i for (i, x) in enumerate(nums) }
    vis = set()
    for j, y in enumerate(nums):
      for k, z in enumerate(nums):
        if (y,z) in vis or (z,y) in vis:
          continue
        if j!=k and y+z in dic and dic[y+z]!=j and dic[y+z]!=k:
          res.append([-y-z,y,z])
          vis.add((-y-z,y))
          vis.add((-y-z,z))
          vis.add((y,z))
    return res