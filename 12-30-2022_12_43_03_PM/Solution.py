# https://leetcode.com/problems/all-paths-from-source-to-target

class Solution:
    def allPathsSourceTarget(self, graph):
        n = len(graph)

        def dfs(k):
            nonlocal n
            if k == n-1:
                return [[k]]
            if not graph[k]:
                return [[]]
            sol = []
            for l in graph[k]:
                for sub in dfs(l):
                    if sub:
                        sol.append([k] + sub)
            return sol
        
        return dfs(0)
                
                    
        
