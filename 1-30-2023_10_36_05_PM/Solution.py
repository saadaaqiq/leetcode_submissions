# https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for x, y in intervals:
            if not res:
                res.append([x,y])
            else:
                a, b = x, y
                while res and (res[-1][0] <= a <= res[-1][1] or res[-1][0] <= b <= res[-1][1]):
                    u,v = res.pop()
                    a, b = min(a,u), max(b,v)
                res.append([a,b])
        return res
