# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero

class Solution:
    def minReorder(self, n: int, edges: List[List[int]]) -> int:
        
        original_edges = set([(edge[0], edge[1]) for edge in edges])
        res = -1

        adj = collections.defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        vis = set()
        
        def dfs(node, parent):
            nonlocal res
            if (node, parent) not in original_edges:
                res += 1
            vis.add(node)
            for neighbor in adj[node]:
                if neighbor not in vis:
                    dfs(neighbor, node)
            
        dfs(0, -1)

        return res