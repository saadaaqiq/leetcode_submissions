# https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
        adj = collections.defaultdict(list)
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        vis = [False] * n
        res = 0
        total = n

        for i in range(n):
            if vis[i]:
                continue
            c = 0
            q = collections.deque([i])
            while q:
                x = q.popleft()
                if vis[x]:
                    continue
                vis[x] = True
                c += 1
                for y in adj[x]:
                    q.append(y)
            res += c * (total - c)
            total -= c 
        
        return res





            
            