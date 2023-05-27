# https://leetcode.com/problems/paint-house-ii

class Solution:
  def minCostII(self, costs: List[List[int]]) -> int:
    cache = [0] * len(costs[0])
    for i in range(len(costs)-1, -1, -1):
      heap = [costs[i][j] + cache[j] for j in range(len(costs[0]))]
      heapq.heapify(heap)
      smallest = heapq.heappop(heap)
      secondSmallest = heapq.heappop(heap)
      for j in range(len(costs[0])):
        cache[j] = secondSmallest if costs[i][j] + cache[j] == smallest else smallest
    return min(cache)
