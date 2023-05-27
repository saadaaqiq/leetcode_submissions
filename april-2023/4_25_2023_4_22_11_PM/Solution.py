# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = collections.defaultdict(list)
        for x, y in edges:
            adj[y].append(x)
        
        stack = []
        vis = set()

        def dfs(y):
            vis.add(y)
            for x in adj[y]:
                if x not in vis:
                    dfs(x)
            stack.append(y)

        answer = [[] for _ in range(n)]

        for i in range(n):
            dfs(i)
            stack.pop()
            answer[i] = sorted(stack.copy())
            stack.clear()
            vis.clear()

        return answer