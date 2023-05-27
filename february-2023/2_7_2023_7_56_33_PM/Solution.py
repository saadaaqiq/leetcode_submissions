# https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid

class Solution:
    def minCost(self,s,h,rc,cc):
        return sum(rc[min(s[0],h[0]):max(s[0],h[0])+1]) - rc[s[0]] + \
                sum(cc[min(s[1],h[1]):max(s[1],h[1])+1]) - cc[s[1]]
                