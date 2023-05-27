# https://leetcode.com/problems/course-schedule-ii

class Solution:
  
  def findOrder(self, n: int, edges: List[List[int]]) -> List[int]:
    
    dic = { k : set() for k in range(n) }
    
    for course, prereq in edges:
      dic[course].add(prereq)
      
    visited = set()
    order = []
    taken = set()
    
    def dfs(course):
      if course in visited:
        return False
      if course in taken:
        return True
      visited.add(course)
      for prereq in dic[course]:
        if not dfs(prereq):
          return False
      visited.remove(course)
      taken.add(course)
      order.append(course)
      return True
      
    for i in range(n):
      if not dfs(i):
        return []
    
    return order