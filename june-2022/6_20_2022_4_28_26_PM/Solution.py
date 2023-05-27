# https://leetcode.com/problems/top-k-frequent-elements

class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    dic = {}
    for num in nums:
      if num not in dic:
        dic[num] = 0
      dic[num] -= 1
    c = 0
    heap = []
    for key in dic:
      heap.append((dic[key], c, key))
      c += 1
    heapq.heapify(heap)
    res = []
    for i in range(k):
      res.append(heapq.heappop(heap)[2])
    return res
    