# https://leetcode.com/problems/min-cost-climbing-stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mincost = [0]*len(cost)
        for i in range(len(cost)-1, -1, -1):
            mincost[i] = cost[i] + min(mincost[i+1] if i+1<len(cost) else 0, mincost[i+2] if i+2<len(cost) else 0)
        return min(mincost[0], mincost[1])
        
        
        
        
