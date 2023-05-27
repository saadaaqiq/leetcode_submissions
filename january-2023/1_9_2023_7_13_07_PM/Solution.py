# https://leetcode.com/problems/max-points-on-a-line

class Line:
    
    def __init__(self, p1, p2):
        self.x1 = p1[0]
        self.y1 = p1[1]
        self.x2 = p2[0]
        self.y2 = p2[1]
        self.vertical = (self.x1 == self.x2)
        self.a = (self.y2-self.y1)/(self.x2-self.x1) if not self.vertical else 0
        self.b = self.y1 - (self.a * self.x1) if not self.vertical else 0
        self.vertical_x = self.x1 if self.vertical else 0
        self.size = 2
    
    def add_point(self, p):
        x, y = p
        B1 = (x != self.x1 or y != self.y1)
        B2 = (x != self.x2 or y != self.y2)
        B3 = ((self.vertical and self.vertical_x == x) or (not self.vertical and abs(self.a * x + self.b - y) <= 0.00001))
        if B1 and B2 and B3:
            self.size += 1
        return self.size

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 1
        vis = set()
        for i in range(n):
            for j in range(n):
                if i == j or (i,j) in vis or (j,i) in vis:
                    continue
                vis.add((i,j))
                line = Line(points[i], points[j])
                for k in range(n):
                    if k == i or k == j or (k,i) in vis or (k,j) in vis or (j,k) in vis or (i,k) in vis:
                        continue
                    pre_size = line.size
                    line.add_point(points[k])
                    post_size = line.size
                    if post_size - pre_size > 0:
                        vis.add((i,k))
                        vis.add((j,k))
                res = max(res, line.size)
        return res
                
                    
                    
                    
                














                
