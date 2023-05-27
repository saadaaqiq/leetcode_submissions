# https://leetcode.com/problems/eliminate-maximum-number-of-monsters

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        heap = []
        for d, s in zip(dist, speed):
            heapq.heappush(heap, d / s)
        res = 0
        for t in range(100001):
            if heap and t < heap[0]:
                res += 1 
                heapq.heappop(heap)
            else:
                return res
        