# https://leetcode.com/problems/course-schedule

class Solution:
    def canFinish(self, n: int, edges: List[List[int]]) -> bool:
        # topological sort with modified dfs
        adj = collections.defaultdict(list)
        # courses that don't need any prerequisites
        entries = set([i for i in range(n)])
        # filling the adjacency dict and removing those 
        # that need prereqs from entries
        for crs, pre in edges:
            adj[pre].append(crs)
            if crs in entries:
                entries.remove(crs)
        
        res = 0
        vis = set()
        cyc = set()

        def dfs(pre):
            nonlocal res
            # once a course is visited it doesn't get revisited
            vis.add(pre)
            # cycle detection, add a course, then remove it
            cyc.add(pre)
            for crs in adj[pre]:
                # if the child is in a cycle, just return
                if crs in cyc:
                    return
                # if the child hasn't been visited, go there
                if crs not in vis:
                    dfs(crs)
            # children of "pre" have been explored so remove it
            cyc.remove(pre)
            # if we made it here (aka no cycle), add the "pre" to the results
            res += 1

        # executing the modified dfs on the courses that 
        # don't have prereqs
        for pre in entries:
            if pre not in vis:
                dfs(pre)

        return res == n
