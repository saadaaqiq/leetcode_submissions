# https://leetcode.com/problems/partition-labels

class Solution:

  def partitionLabels(self, s: str) -> List[int]:

    dic = {}

    for i,c in enumerate(s):
      if c not in dic:
        dic[c] = (i,i)
      else:
        dic[c] = (dic[c][0], i)

    old = -1,-1
    res = []

    for i, (x,y) in enumerate(dic.values()):
      if x >= old[1]:
        old = x,y
        res.append(old[1] - old[0] + 1)
      else:
        old = (min(old[0],x), max(old[1],y))
        res[-1] = old[1] - old[0] + 1

    return res
      