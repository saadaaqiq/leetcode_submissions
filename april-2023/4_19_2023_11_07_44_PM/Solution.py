# https://leetcode.com/problems/parallel-courses

class Solution:
    def minimumSemesters(self, n: int, edges: List[List[int]]) -> int:
        # building the adjacency list
        adj = collections.defaultdict(list)
        for i, j in edges:
            adj[i].append(j)
        # indegrees for a modified version
        # of Kahn's algorithm
        in_degree = [0] * (n+1)
        for i, j in edges:
            in_degree[j] += 1
        q = collections.deque()
        # add the nodes with indegree 0 
        # to the queue, aka the courses that 
        # don't depend upon any other courses
        for i in range(1, n+1):
            if in_degree[i] == 0:
                q.append(i)
        # append the delimiter to know when a 
        # semester has ended
        q.append(0)
        # a counter to check if all the courses
        # have been taken
        cnt = 0
        # the semester counter "res" and result to return
        res = 0
        while q:
            u = q.popleft()
            # if u is the delimiter, increment results
            # if queue is not empty it has other courses
            # so add another delimiter after those as well
            if u == 0:
                res += 1
                # delimiter, comes between semesters
                # checks if the q is not empty to not
                # go into an infinite loop of adding 0's
                if q:
                    q.append(0)
                continue
            # decrement the indegree of all the neighbors
            # of the current node
            # and those that now have an indegree of 0 get 
            # added to the queue (it's basically like bfs)
            for j in adj[u]:
                in_degree[j] -= 1
                if in_degree[j] == 0:
                    q.append(j)
            # increment the counter
            cnt += 1
        # if the counter is less than n then we can't
        # take all the courses
        # else we return the number of semesters res
        return res if cnt == n else -1
 
