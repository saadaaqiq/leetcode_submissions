# https://leetcode.com/problems/valid-perfect-square

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, 46341
        while l < r:
            mid = (l+r)//2
            if mid*mid<num:
                l = mid + 1
            elif mid*mid>num:
                r = mid
            else:
                return True
        return False