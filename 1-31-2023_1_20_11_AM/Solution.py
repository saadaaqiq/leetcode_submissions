# https://leetcode.com/problems/meeting-rooms-ii

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        S = sorted([I[0] for I in intervals])
        E = sorted([I[1] for I in intervals])
        i, j = 0, 0
        count = 0
        res = 0
        while i < len(S) and j < len(E):
            if S[i] < E[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            res = max(res, count)
        return res