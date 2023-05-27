# https://leetcode.com/problems/maximum-xor-after-operations

class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        res = 0
        for v in nums:
            res |= v
        return res
