# https://leetcode.com/problems/insert-interval

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        starts, ends = list(zip(*intervals))
        s = bisect_left(ends, newInterval[0])
        e = bisect_right(starts, newInterval[1])
        print((s,e))
        return intervals[:s] + [[min(intervals[s][0], newInterval[0]) if s<e else newInterval[0], max(intervals[e-1][1], newInterval[1]) if s<e else newInterval[1]]] + intervals[e:]
