# https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n, s, res = len(nums), 0, max(nums)
        if res <= 0:
            return res
        for i in range(n):
            s = max(0, s + nums[i])
            res = max(res, s)
        return res