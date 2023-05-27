# https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for x, y in intervals:
            if not res:
                res.append([x,y])
            else:
                if x > res[-1][1]:
                    res.append([x, y])
                else:
                    res[-1][1] = max(res[-1][1], y)
        return res