# https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks

class Solution:
  def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
    heap = []
    for i in range(len(capacity)):
      heapq.heappush(heap, (capacity[i]-rocks[i]))
    res = 0
    while heap:
      toAdd = heapq.heappop(heap)
      if additionalRocks >= toAdd:
        res += 1
        additionalRocks -= toAdd
      else:
        break
    return res