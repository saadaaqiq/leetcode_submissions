# https://leetcode.com/problems/min-cost-to-connect-all-points

class Solution:
   def minCostConnectPoints(self, P: List[List[int]]) -> int:

      def man(p1, p2):
         return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

      n = len(P)
      heap = []
      for i in range(1, n):
         heapq.heappush(heap, (man(P[0], P[i]), 0, i))
      vis = set([0])
      res = 0

      while heap and len( vis) < len(P):
         cost, i, j = heapq.heappop(heap)
         if j in vis:
            continue
         res += cost
         vis.add(j)
         for k in range(n):
            if k not in vis:
               heapq.heappush(heap, (man(P[k], P[j]), j, k))

      return res
