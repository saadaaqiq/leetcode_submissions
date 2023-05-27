# https://leetcode.com/problems/course-schedule

class Solution:
    
    def canFinish(self, n: int, edges: List[List[int]]) -> bool:
        
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
                return False
        return True
        
        
        
        
        
        
        
        
        
        
        
        