# https://leetcode.com/problems/two-city-scheduling

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs)
        res = sum([costs[i][(0 if i < N//2 else 1)] for i in range(N)])
        while True:
            boo = False
            for i in range(N//2):
                for j in range(N//2, N):
                    if costs[j][0] + costs[i][1] - costs[i][0] - costs[j][1] < 0:
                        res += costs[j][0] - costs[i][0] - costs[j][1] + costs[i][1]
                        costs[i], costs[j] = costs[j], costs[i]
                        boo = True
            if not boo:
                return res

