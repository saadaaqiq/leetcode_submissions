# https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        arr = [1,2]
        while len(arr) < n:
            arr.append(arr[-1]+arr[-2])
        return arr[-1]