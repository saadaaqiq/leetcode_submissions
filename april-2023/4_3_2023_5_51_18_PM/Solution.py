# https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        if 0 < n < 3:
            return n
        prev, cur = 1, 2
        for i in range(3,n+1):
            prev, cur = cur, prev + cur
        return cur