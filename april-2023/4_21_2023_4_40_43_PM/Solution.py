# https://leetcode.com/problems/find-eventual-safe-states

class Solution:
    def eventualSafeNodes(self, graph):
        res = set()
        vis = set()

        def dfs(x):
            if x in res:
                return True
            if x in vis:
                return False
            vis.add(x)
            for y in graph[x]:
                if not dfs(y):
                    return False
            vis.remove(x)
            res.add(x)
            return True
        
        for i in range(len(graph)):
            dfs(i)
        return sorted(list(res))
