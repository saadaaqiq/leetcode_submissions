# https://leetcode.com/problems/two-city-scheduling

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs)
        a, b = 0, 0
        for i in range(N):
            if i < N//2:
                a += costs[i][0]
            else:
                b += costs[i][1]

        while True:
            boo = False
            for i in range(N//2):
                for j in range(N//2, N):
                    if a - costs[i][0] + costs[j][0] + b - costs[j][1] + costs[i][1] < a + b:
                        a = a + costs[j][0] - costs[i][0]
                        b = b - costs[j][1] + costs[i][1]
                        costs[i], costs[j] = costs[j], costs[i]
                        boo = True
            if not boo:
                return a + b


        
