# https://leetcode.com/problems/course-schedule-ii

class Solution:
    def findOrder(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        indeg = [0] * n
        for crs, pre in edges:
            adj[pre].append(crs)
            indeg[crs] += 1
        q = collections.deque()
        stack = []
        for crs in range(n):
            if indeg[crs] == 0:
                q.append(crs)
        count = 0
        while q:
            crs = q.popleft()
            if indeg[crs] == 0:
                stack.append(crs)
            for dep in adj[crs]:
                indeg[dep] -= 1
                count += 1
                if indeg[dep] == 0:
                    q.append(dep)
        return stack if count == len(edges) else []