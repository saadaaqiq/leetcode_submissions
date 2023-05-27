# https://leetcode.com/problems/tree-diameter

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        res = -inf
        adj = collections.defaultdict(list)
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        vis = set()
        def dfs(node):
            nonlocal res
            vis.add(node)
            fmax, smax = 0, 0
            for neighbor in adj[node]:
                if neighbor not in vis:
                    d = 1 + dfs(neighbor)
                    if d >= fmax:
                        smax = fmax
                        fmax = d
                    elif d > smax:
                        smax = d
            vis.remove(node)
            res = max(res, fmax + smax)
            return max(fmax, smax)
        dfs(0)
        return res