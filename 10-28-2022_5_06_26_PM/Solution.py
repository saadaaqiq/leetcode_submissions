# https://leetcode.com/problems/3sum

class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    cnt = Counter(nums)
    for k in cnt: 
      cnt[k] = min(cnt[k], 3)
    vis=set()
    for a in cnt:
      for b in cnt:
        c = -a-b
        if c in cnt and ((a == b and a!=c and cnt[a]>=2) or (a == b and a == c and cnt[a]>=3) or (a != b and b != c and a != c)):
          vis.add((a,b,c))
    res = []
    while vis:
      a,b,c = vis.pop()
      comb = [(a,c,b), (b,a,c), (b,c,a), (c,a,b), (c,b,a)]
      for co in comb:
        if co in vis:
          vis.remove(co)
      res.append([a,b,c])
    return res
      