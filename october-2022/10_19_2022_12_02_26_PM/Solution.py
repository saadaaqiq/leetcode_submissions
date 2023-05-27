# https://leetcode.com/problems/top-k-frequent-words

class Solution:
  def topKFrequent(self, words: List[str], k: int) -> List[str]:
    dic = {}
    for w in words:
      if w not in dic:
        dic[w] = 0
      dic[w] += 1
    res = [(dic[w],w) for w in dic]
    res.sort(reverse=True)
    i = 0
    result = []
    curr = []
    print(res)
    while i < len(res):
      curr.append(res[i][1])
      j = i+1
      while j < len(res) and res[j][0] == res[i][0]:
        curr.append(res[j][1])
        j += 1
      i = j
      while curr:
        result.append(curr.pop())
    return result[:k]