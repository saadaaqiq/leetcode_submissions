# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        heapq.heapify(points)
        (pl, pr), res = heapq.heappop(points), 1
        while points:
            cl, cr = heapq.heappop(points)
            pl, pr, res = (pl, cr, res) if cr <= pr else ((cl, cr, res + 1) if cl > pr else (cl, pr, res))
        return res