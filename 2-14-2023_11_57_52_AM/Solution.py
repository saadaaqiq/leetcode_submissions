# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range

class Solution:
    def countOdds(self, l: int, h: int) -> int:
        return (h-l)//2 + (1 if l%2 or h%2 else 0)