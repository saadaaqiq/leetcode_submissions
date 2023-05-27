# https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition

class Solution:
    def minNumberOfHours(self, en: int, ex: int, energy: List[int], experience: List[int]) -> int:
        res = 0
        for a,b in zip(energy, experience):
            if en - a <= 0:
                res += a - en + 1
                en += a - en + 1
            if ex - b <= 0:
                res += b - ex + 1
                ex += b - ex + 1
            en -= a 
            ex += b
        return res