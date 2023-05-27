# https://leetcode.com/problems/insert-interval

class Solution:

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if not intervals:
            return [newInterval]

        def cut_left(arr, x):
            l, r = 0, len(arr)
            while l<r:
                mid = (l+r)//2
                if arr[mid] < x:    
                    l = mid + 1
                else:               
                    r = mid
            return l

        def cut_right(arr, x):
            l, r = 0, len(arr)
            while l<r:
                mid = (l+r)//2
                if x < arr[mid]:    
                    r = mid
                else:               
                    l = mid + 1
            return l

        s = cut_left([interval[1] for interval in intervals], newInterval[0])
        e = cut_right([interval[0] for interval in intervals], newInterval[1])

        return intervals[:s] + [[min(intervals[s][0], newInterval[0]) if s<e else newInterval[0], max(intervals[e-1][1], newInterval[1]) if s<e else newInterval[1]]] + intervals[e:]