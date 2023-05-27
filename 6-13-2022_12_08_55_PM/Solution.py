# https://leetcode.com/problems/meeting-rooms-ii

class Solution:
  def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    starts, ends = [x[0] for x in intervals], [x[1] for x in intervals]
    starts.sort()
    ends.sort()
    i,j,c,m = 0,0,0,0
    while i < len(starts) and j < len(ends):
      if starts[i] < ends[j]:
        c += 1
        i += 1
      else:
        c -= 1
        j += 1
      m = max(m,c)
    return m
    