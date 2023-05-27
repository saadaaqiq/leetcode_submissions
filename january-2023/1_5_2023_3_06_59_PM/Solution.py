# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        heapq.heapify(points)
        res = 1
        pl, pr = points[0]
        while points:
            cl, cr = heapq.heappop(points)
            if cr <= pr:
                pr = cr
            else:
                if cl <= pr:
                    pl = cl
                else:
                    res += 1
                    pl, pr = cl, cr
        return res