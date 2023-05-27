# https://leetcode.com/problems/minimum-cost-to-connect-sticks

class Solution:
  def connectSticks(self, sticks: List[int]) -> int:
    heapq.heapify(sticks)
    cost = 0
    while len(sticks) >= 2:
      a = heapq.heappop(sticks)
      b = heapq.heappop(sticks)
      cost += a + b
      heapq.heappush(sticks, a + b)
    return cost