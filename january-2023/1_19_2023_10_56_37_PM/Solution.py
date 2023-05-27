# https://leetcode.com/problems/maximum-sum-circular-subarray

class Solution:
    def maxSubarraySumCircular(self, arr: List[int]) -> int:
        
        def kadanes(nums, inv):
            cs, ms = 0, max(nums) if not inv else min(nums)
            for num in nums:
                cs = num + (cs if (cs > 0 and not inv) or (cs < 0 and inv) else 0)
                ms = max(ms, cs) if not inv else min(ms, cs)
            return ms if not inv else sum(nums) - ms
        
        a = kadanes(arr, False)
        b = kadanes(arr, True)

        if a < 0:
            return a
        else:
            return max(a, b)

        

