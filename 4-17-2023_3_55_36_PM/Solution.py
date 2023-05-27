# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        res = []
        m = max(candies)
        for c in candies:
            res.append(c + extraCandies >= m)
        return res