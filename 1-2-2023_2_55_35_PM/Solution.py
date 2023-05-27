# https://leetcode.com/problems/single-threaded-cpu

class Solution:
  def getOrder(self, tasks):
    n = len(tasks)
    res = []
    for j in range(n):
      tasks[j].append(j)
    tasks.sort()
    i = 0
    time = 0
    heap = []
    while i < n or heap:
      if not heap and tasks[i][0] > time:
        time = tasks[i][0]
      while i < n and tasks[i][0] <= time:
        heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
        i += 1
      dur, ind = heapq.heappop(heap)
      res.append(ind)
      time += dur
    return res