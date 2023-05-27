# https://leetcode.com/problems/top-k-frequent-words

class Solution:
  def topKFrequent(self, words: List[str], k: int) -> List[str]:
    count = Counter(words)
    h = []
    for w in count:
      heapq.heappush(h, (-count[w], w))
    res = []
    for i in range(k):
      res.append(heapq.heappop(h)[1])
    return res