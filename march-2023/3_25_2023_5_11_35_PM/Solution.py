# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        adj = collections.defaultdict(list)
        for src, dst, dist in roads:
            adj[src].append(dst)
            adj[dst].append(src)
        vis = set()
        def dfs(city):
            vis.add(city)
            for neighbor in adj[city]:
                if neighbor not in vis:
                    dfs(neighbor)
        dfs(1)
        res = math.inf
        for src, dst, dist in roads:
            if src in vis or dst in vis:
                res = min(res, dist)
        return res

            

