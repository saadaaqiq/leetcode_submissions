# https://leetcode.com/problems/course-schedule

class Solution(object):
    def canFinish(self, n, edges):
        # Kahn's algorithm
        indeg = [0]*n
        adj = collections.defaultdict(list)
        for crs, pre in edges:
            adj[pre].append(crs)
            indeg[crs] += 1
            
        q = deque()
        for crs in range(n):
            if indeg[crs] == 0:
                q.append(crs)

        res = 0
        while q:
            pre = q.popleft()
            for crs in adj[pre]:
                indeg[crs] -= 1
                res += 1
                if indeg[crs] == 0:
                    q.append(crs)

        return res == len(edges)