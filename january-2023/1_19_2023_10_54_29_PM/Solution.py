# https://leetcode.com/problems/maximum-sum-circular-subarray

class Solution:
    def maxSubarraySumCircular(self, arr: List[int]) -> int:
        
        def max_kadanes(nums):
            cs, ms = 0, max(nums)
            for num in nums:
                cs = num + (cs if cs > 0 else 0)
                ms = max(ms, cs)
            return ms
        
        def min_kadanes(nums):
            cs, ms = 0, min(nums)
            for num in nums:
                cs = num + (cs if cs < 0 else 0)
                ms = min(ms, cs)
            return ms

        a = max_kadanes(arr)
        b = min_kadanes(arr)

        if a < 0:
            return a
        else:
            return max(a, sum(arr) - b)

        

