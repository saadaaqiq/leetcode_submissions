# https://leetcode.com/problems/course-schedule-ii

class Solution:
  
  def findOrder(self, n: int, edges: List[List[int]]) -> List[int]:
    
    dic = { k : set() for k in range(n) }
    
    for course, prereq in edges:
      dic[course].add(prereq)
      
    visited = set()
    order = []
    
    def dfs(course):
      if course in visited:
        return False
      if not dic[course]:
        if course not in order:
          order.append(course)
        return True
      visited.add(course)
      for prereq in list(dic[course]):
        if not dfs(prereq):
          return False
        else:
          dic[course].remove(prereq)
      visited.remove(course)
      if course not in order:
        order.append(course)
      return True
      
    for i in range(n):
      if not dfs(i):
        return []
    
    return order