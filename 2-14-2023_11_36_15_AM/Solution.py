# https://leetcode.com/problems/shortest-path-with-alternating-colors

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        for s, d in redEdges:
            adj[s].append((d, 1))
        for s, d in blueEdges:
            adj[s].append((d, -1))
        res = [math.inf] * n
        q = collections.deque([(0, 0, 0)])
        vis = set()
        while q:
            node, prev_color, distance = q.popleft()
            res[node] = min(res[node], distance)
            vis.add((node, prev_color))
            for neighbor, color in adj[node]:
                if neighbor != 0 and (neighbor, color) not in vis and color != prev_color:
                    q.append((neighbor, color, distance + 1))

        for i in range(n):
            if res[i] > 10**7:
                res[i] = -1
        return res
            
        