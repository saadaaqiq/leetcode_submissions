# https://leetcode.com/problems/k-closest-points-to-origin

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        for x,y in points:
            heapq.heappush(arr, (-sqrt(x*x + y*y), [x,y]))
        while len(arr) > k:
            heapq.heappop(arr)
        return list(zip(*arr))[1]
