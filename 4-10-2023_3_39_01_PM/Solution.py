# https://leetcode.com/problems/largest-color-value-in-a-directed-graph

from collections import Counter

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        if not edges:
            return 1
        
        adj = collections.defaultdict(list)
        for x, y in edges:
            adj[x].append(y)

        vis = set()
        @cache
        def dfs(node):
            if node in vis:
                return None
            counter = Counter()
            if not adj[node]:
                counter[colors[node]] += 1
                return counter
            for neighbor in adj[node]:
                vis.add(node)
                n_counter = dfs(neighbor)
                if not n_counter:
                    return None
                for c in n_counter:
                    counter[c] = max(counter[c], n_counter[c])
                vis.remove(node)
            counter[colors[node]] += 1
            return counter

        res = -1

        for node in range(len(colors)):
            if not dfs(node):
                return -1
            res = max(res, max(dfs(node).values()))
    
        return res






        