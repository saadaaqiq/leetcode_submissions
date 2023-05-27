# https://leetcode.com/problems/meeting-rooms

class Solution:
  def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
    intervals = sorted(intervals, key= lambda x: x[0])
    for k in range(len(intervals)-1):
      i,j = intervals[k]
      m,n = intervals[k+1]
      if m < j:
        return False
    return True