# https://leetcode.com/problems/minimum-bit-flips-to-convert-number

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = 0
        while start or goal:
            res += (start & 1) ^ (goal & 1)
            start >>= 1
            goal >>= 1
        return res