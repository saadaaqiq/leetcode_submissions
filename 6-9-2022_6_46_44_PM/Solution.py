# https://leetcode.com/problems/meeting-rooms-ii

class Solution:
  def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x: x[0])
    dic={}
    for i,j in intervals:
      if (i,j) not in dic:
        dic[(i,j)]=0
      dic[(i,j)] += 1
    c = 0
    while dic:
      last = -1
      for i,j in intervals:
        if (i,j) not in dic:
          continue
        if last == -1:
          last = i
        if i >= last:
          last = j
          dic[(i,j)]-=1
          if dic[(i,j)] == 0:
            dic.pop((i,j))
      c += 1
    return c
      