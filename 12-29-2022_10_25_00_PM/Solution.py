# https://leetcode.com/problems/single-threaded-cpu

class Solution:
  def getOrder(self, tasks: List[List[int]]) -> List[int]:
    h = []
    res = []
    n = len(tasks)

    for i in range(n):
      tasks[i].append(i)
    tasks.sort()
        
    ts = 0
    j = 0
        
    while j < n or h:
      if not h and ts < tasks[j][0]:
        ts = tasks[j][0]     
      while j < n and ts >= tasks[j][0]:
        a, b, k = tasks[j]
        heapq.heappush(h, (b, k))
        j += 1
      b, k = heapq.heappop(h)
      ts += b
      res.append(k)
        
    return res