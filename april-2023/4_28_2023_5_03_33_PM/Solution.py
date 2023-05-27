# https://leetcode.com/problems/two-city-scheduling

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs)
        costs.sort(key=lambda x:x[0]-x[1])
        return sum([x[(0 if i<N//2 else 1)] for (i,x) in enumerate(costs)])

