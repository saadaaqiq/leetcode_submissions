# https://leetcode.com/problems/relative-ranks

class Solution:
  def findRelativeRanks(self, score: List[int]) -> List[str]:
    n = len(score)
    dic = { score[i] : i for i in range(len(score)) }
    heapq.heapify(score)
    i = 0
    while score:
      k = heappop(score)
      dic[str(n-i)] = dic[k]
      del dic[k]
      i+=1
    if '1' in dic:
      dic["Gold Medal"] = dic['1']
      del dic['1']
    if '2' in dic:
      dic["Silver Medal"] = dic['2']
      del dic['2']
    if '3' in dic:
      dic["Bronze Medal"] = dic['3']
      del dic['3']
    res = ['' for i in range(n)]
    for k in dic:
      res[dic[k]] = k
    return res
    