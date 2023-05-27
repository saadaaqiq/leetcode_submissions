# https://leetcode.com/problems/sign-of-the-product-of-an-array

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for v in nums:
            if v == 0:
                res = 0
            elif v < 0:
                res *= -1
        return res