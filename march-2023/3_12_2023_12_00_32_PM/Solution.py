# https://leetcode.com/problems/koko-eating-bananas

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def can_finish(k):
            c = 0
            for p in piles:
                c += math.ceil(p / k)
                if c > h:
                    return False
            return True


        l, r = 1, 10**9 + 1
        while l < r:
            mid = (l+r) // 2
            if can_finish(mid):
                r = mid
            else:
                l = mid + 1
        
        return l