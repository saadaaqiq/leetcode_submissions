# https://leetcode.com/problems/the-skyline-problem

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        h = []
        cl, cr, ch = -1, -1, 0
        for i, building in enumerate(buildings):
            left, right, height = building
            heapq.heappush(h, (left, height, i, True))
            heapq.heappush(h, (right, height, i, False))
        res = []
        cur_highest = []
        heapq.heappush(cur_highest, (0, -1))
        closed = set()
        while h:
            x, height, i, opened = heapq.heappop(h)
            if opened:
                heapq.heappush(cur_highest, (-height, i))
            else:
                closed.add(i)
            while cur_highest and cur_highest[0][1] in closed:
                heapq.heappop(cur_highest)
            if height >= -cur_highest[0][0]:
                if res and res[-1][0] == x:
                    res.pop()
                if not res or -cur_highest[0][0] != res[-1][1]:
                    res.append([x, -cur_highest[0][0]])
        return res
        

        