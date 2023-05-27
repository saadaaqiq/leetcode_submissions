# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        dic = collections.defaultdict(list)
        for x, y, s in roads:
            dic[x].append((y, s))
            dic[y].append((x, s))

        vis = {i:math.inf for i in range(1, n+1)}
        q = collections.deque()

        for city, score in dic[1]:
            q.append((city, score))

        while q:
            city, score = q.popleft()
            if score >= vis[city]:
                continue
            vis[city] = score
            for neighbour, s in dic[city]:
                q.append((neighbour, min(s, score)))

        return vis[n]
            



            

