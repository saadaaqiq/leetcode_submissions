# https://leetcode.com/problems/insert-interval

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        s = bisect_left([interval[1] for interval in intervals], newInterval[0])
        e = bisect_right([interval[0] for interval in intervals], newInterval[1])
        return intervals[:s] + [[min(intervals[s][0], newInterval[0]) if s<e else newInterval[0], max(intervals[e-1][1], newInterval[1]) if s<e else newInterval[1]]] + intervals[e:]
