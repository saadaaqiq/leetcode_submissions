# https://leetcode.com/problems/course-schedule-ii

class Solution:
  def findOrder(self, n: int, edges: List[List[int]]) -> List[int]:
    
    dic = { k : [] for k in range(n)}
    for course, prereq in edges:
      dic[course].append(prereq)
    visited = set()
        
    def dfs(course):
      if course in visited:
        return False
      if dic[course] == []:
        return True
      visited.add(course)
      for prereq in dic[course]:
        if not dfs(prereq):
          return False
      visited.remove(course)
      dic[course] = []
      return True
        
    for course in range(n):
      if not dfs(course):
        return []
    
    dic = { k : set() for k in range(n)}
    dic2 = { k : set() for k in range(n)}
    for course, prereq in edges:
      dic[course].add(prereq)
      dic2[prereq].add(course)
    order = []
    q = deque([k for k in range(n)])
    while q:
      c = q.popleft()
      if not dic[c]:
        order.append(c)
        for cr in dic2[c]:
          dic[cr].remove(c)
      else:
        q.append(c)
    return order