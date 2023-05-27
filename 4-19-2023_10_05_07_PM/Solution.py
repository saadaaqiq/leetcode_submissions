# https://leetcode.com/problems/parallel-courses

class Solution:
    def minimumSemesters(self, n: int, edges: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        for i, j in edges:
            adj[i].append(j)
        in_degree = [0] * (n+1)
        for i, j in edges:
            in_degree[j] += 1
        q = collections.deque()
        for i in range(1, n+1):
            if in_degree[i] == 0:
                q.append(i)
        q.append(0)
        cnt = 0
        res = 0
        while q:
            u = q.popleft()
            if u == 0:
                res += 1
                if q:
                    q.append(0)
                continue
            for j in adj[u]:
                in_degree[j] -= 1
                if in_degree[j] == 0:
                    q.append(j)
            cnt += 1
        return res if cnt == n else -1
 
