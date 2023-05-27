# https://leetcode.com/problems/longest-cycle-in-a-graph

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        vis = set()
        res = -1
        for i in range(n):
            cur_set = set()
            cur, length = i, 0
            while True:
                if edges[cur] == -1 or edges[cur] in vis:
                    vis |= cur_set                   
                    break
                elif edges[cur] in cur_set:
                    cur_set.add(cur)
                    cur = edges[cur]
                    length += 1
                    pointer = i
                    dist = 0
                    while pointer != cur:
                        pointer = edges[pointer]
                        dist += 1
                    res = max(res, length - dist)
                    vis |= cur_set
                    break
                else:
                    cur_set.add(cur)
                    length += 1
                    cur = edges[cur]
        return res

        