# https://leetcode.com/problems/successful-pairs-of-spells-and-potions

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        for spell in spells:
            t = success/spell
            l, r = 0, len(potions)
            while l < r:
                m = (l+r) // 2
                if potions[m] < t:
                    l = m + 1
                else:
                    r = m
            res.append(len(potions) - l)
        return res