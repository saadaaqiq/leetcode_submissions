# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        res = 0
        cur = -math.inf
        for l,r in points:
            if l > cur:
                res += 1
                cur = r
        return res