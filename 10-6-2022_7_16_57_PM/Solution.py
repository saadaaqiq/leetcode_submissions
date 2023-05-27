# https://leetcode.com/problems/campus-bikes

class Solution:
  def assignBikes(self, workers, bikes):
    distances = [[] for i in range(2000)]
    wS = [False for i in range(len(workers))]
    bS = [False for i in range(len(bikes))]
    for i, w in enumerate(workers):
      for j, b in enumerate(bikes):
        distances[abs(w[0]-b[0])+abs(w[1]-b[1])-1].append((i,j))
    res = [-1] * len(workers)
    for d in distances:
      if not d: continue
      for i, j in d:
        if wS[i] or bS[j]:
          continue
        else:
          res[i] = j
          wS[i] = True
          bS[j] = True
    return res