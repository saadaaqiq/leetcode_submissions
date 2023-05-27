# https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        x, y = initialEnergy, initialExperience
        ene, exp = 0, 0
        for a,b in zip(energy, experience):
            if x - a <= 0:
                ene += a - x + 1
                x += a - x + 1
            if y - b <= 0:
                exp += b - y + 1
                y += b - y + 1
            x -= a 
            y += b
        return ene + exp