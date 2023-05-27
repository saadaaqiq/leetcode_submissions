# https://leetcode.com/problems/max-value-of-equation

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        heap = []
        res = -math.inf
        for l, r in points:
            while heap and l - heap[0][1] > k:
                heapq.heappop(heap)
            if heap:
                res = max(res, l + r - heap[0][0])
            heapq.heappush(heap, (-r + l, l))
        return res


