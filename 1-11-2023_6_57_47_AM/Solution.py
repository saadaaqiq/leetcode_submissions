# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        adj = collections.defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        vis = set()
        def dfs(x):
            vis.add(x)
            apples = sum([dfs(y) for y in adj[x] if y not in vis]) 
            res = (1 if apples > 0 or hasApple[x] else 0) + apples
            return res
        
        return max(0, 2*(dfs(0)-1))