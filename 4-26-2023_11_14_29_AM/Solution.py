# https://leetcode.com/problems/course-schedule

class Solution:
    def canFinish(self, n: int, edges: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        entries = set([i for i in range(n)])
        for crs, pre in edges:
            adj[pre].append(crs)
            if crs in entries:
                entries.remove(crs)
        
        res = set()
        vis = set()
        cyc = set()

        def dfs(pre):
            vis.add(pre)
            cyc.add(pre)
            for crs in adj[pre]:
                if crs in cyc:
                    return
                if crs not in vis:
                    dfs(crs)
            cyc.remove(pre)
            res.add(pre)

        for pre in entries:
            if pre not in vis:
                dfs(pre)

        return len(res) == n