# https://leetcode.com/problems/maximum-xor-for-each-query

class Solution:
    def getMaximumXor(self, nums: List[int], param: int) -> List[int]:
        xor = functools.reduce(lambda x, y: x^y, nums)
        k = sum([2**i for i in range(20)])
        k >>= 20-param
        res = []
        for i in range(len(nums)-1, -1, -1):
            res.append(xor ^ k)
            xor ^= nums[i]
        return res