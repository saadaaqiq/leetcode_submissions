# https://leetcode.com/problems/max-points-on-a-line

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        return 1 + (max([max(Counter([math.atan2(y2-y1,x2-x1)%math.pi for j,(x2,y2) in enumerate(points) if j!=i]).values()) for i,(x1,y1) in enumerate(points)]) if len(points)>1 else 0)