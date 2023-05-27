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
            arr = [dfs(l) for l in graph[k]]
            sol = []
            for sub in arr:
                for subsub in sub:
                    if subsub:
                        sol.append([k] + subsub)
            return sol
        
        return dfs(0)
                
                    
        
