# https://leetcode.com/problems/max-points-on-a-line

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1: 
            return 1
        res = 0
        for i, (x1,y1) in enumerate(points):
            res = max(res, max(Counter([math.atan2(y2-y1,x2-x1)%math.pi for j,(x2,y2) in enumerate(points) if j!=i]).values()))  
        return res + 1