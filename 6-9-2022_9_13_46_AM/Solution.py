# https://leetcode.com/problems/meeting-rooms

class Solution:
  def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
    s = set()
    for i,j in intervals:
      for k in range(2*i+1,2*j):
        if k in s: 
          return False
        else:
          s.add(k)
    return True
        