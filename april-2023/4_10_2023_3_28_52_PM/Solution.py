# https://leetcode.com/problems/largest-color-value-in-a-directed-graph

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        if not edges:
            return 1
        
        adj = {}
        for x, y in edges:
            if x not in adj:
                adj[x] = []
            if y not in adj:
                adj[y] = []
            adj[x].append(y)

        vis = set()
        @cache        
        def cycle_detection(node):
            if not adj[node]:
                return True
            if node in vis:
                return False
            for neighbor in adj[node]:
                vis.add(node)   
                if not cycle_detection(neighbor):
                    return False
                vis.remove(node)
            return True
            
        
        for x in adj:
            if not cycle_detection(x):
                return -1

        sources = set([i for i in range(len(colors))])
        for x in adj:
            for y in adj[x]:
                if y in sources:
                    sources.remove(y)
                
        def get_max_and_index(cur):
            ind = -1
            mc = 0
            for i, c in enumerate(cur):
                if c > mc:
                    ind, mc = i, c
            return (ind, mc)

        res = -1

        @cache
        def dfs(node):
            nonlocal res
            counter = collections.Counter()
            if not adj[node]:
                counter[colors[node]] += 1
                return counter
            for neighbor in adj[node]:
                neighbor_counter = dfs(neighbor)
                for c in neighbor_counter:
                    counter[c] = max(counter[c], neighbor_counter[c])
            counter[colors[node]] += 1
            return counter

        for node in sources:
            counter = dfs(node)
            res = max(max(counter.values()), res)

        return res