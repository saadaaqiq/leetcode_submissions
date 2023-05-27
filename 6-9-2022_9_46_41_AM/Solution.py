# https://leetcode.com/problems/meeting-rooms

class Solution:
  def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
    arr = [0] * 3000003
    for i,j in intervals:
      arr[3*i+1] -= 1
      arr[3*j-1] += 1
    b = False
    for i in range(len(arr)):
      if arr[i] < -1 or arr[i] > 1:
        return False
      if arr[i] == -1:
        if not b:
          b = True
        else:
          return False
      if arr[i] == 1:
        if b:
          b = False
        else:
          return False
    return True
    
      