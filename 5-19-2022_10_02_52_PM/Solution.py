# https://leetcode.com/problems/last-stone-weight

class Solution:
  def lastStoneWeight(self, stones: List[int]) -> int:
    stones = [-i for i in stones]
    heapq.heapify(stones)
    
    while stones:
      y = -heappop(stones)
      if not stones:
        return y
      x = -heappop(stones)
      if x < y:
        heappush(stones, -(y-x))
    
    return 0
    