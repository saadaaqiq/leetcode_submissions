# https://leetcode.com/problems/meeting-rooms-ii

class Solution:
    def minMeetingRooms(self, arr: List[List[int]]) -> int:
        starts = collections.defaultdict(int)
        ends = collections.defaultdict(int)
        mini, maxi = math.inf, -math.inf
        for s, e in arr:
            mini = min(mini, s)
            maxi = max(maxi, e)
            starts[s] += 1
            ends[e] += 1
        res = 0
        curr = 0
        for i in range(mini, maxi+1):
            curr += starts[i]
            curr -= ends[i]
            res = max(res,curr)
        return res