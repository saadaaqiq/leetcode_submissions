# https://leetcode.com/problems/path-crossing

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        vis = set()
        d = {"N": (0,1), "S": (0,-1), "W": (-1,0), "E": (1,0)}
        
        def f(p, c):
            return (p[0]+d[c][0], p[1]+d[c][1])
        
        curr = (0,0)
        vis.add(curr)

        for c in path:
            curr = f(curr, c)
            if curr in vis:
                return True
            vis.add((curr))
        
        return False