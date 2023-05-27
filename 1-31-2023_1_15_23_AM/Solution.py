# https://leetcode.com/problems/meeting-rooms-ii

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        arr = []
        for x, y in intervals:
            arr.append((x,1))
            arr.append((y,0))
        arr.sort()
        res = 0
        curr = 0
        for u, v in arr:
            if v == 1:
                curr += 1
            else:
                curr -= 1
            res = max(res, curr)
        return res