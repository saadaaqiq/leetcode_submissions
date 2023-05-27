# https://leetcode.com/problems/maximum-xor-for-each-query

class Solution:
    def getMaximumXor(self, nums: List[int], param: int) -> List[int]:
        n = len(nums)
        xor = 0
        for num in nums:
            xor ^= num
        k = 2 ** (param-1)
        c = 0
        while ((k>>c) & 1) == 0:
            k |= 1<<c
            c += 1
        res = []
        p = n-1
        for i in range(n):
            # so let q be such as: xor ^ q maximized
            # we have xor ^ (xor ^ k) = k, and k is the max such as k < 2**param
            # so xor^k is the thing to add to the res
            res.append(xor ^ k)
            xor ^= nums[p]
            p -= 1
        return res