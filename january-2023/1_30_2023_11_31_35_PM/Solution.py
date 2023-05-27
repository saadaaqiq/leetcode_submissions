# https://leetcode.com/problems/non-overlapping-intervals

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        x, y = intervals.pop()
        while intervals:
            while intervals and (intervals[-1][0] <= x < intervals[-1][1] or intervals[-1][0] < y <= intervals[-1][1]):
                intervals.pop()
                res += 1
            if intervals:
                x, y = intervals.pop()
        return res


