# https://leetcode.com/problems/maximum-sum-circular-subarray

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        x, max_s = 0, max(nums)
        y, min_s = 0, min(nums)
        s = 0
        for num in nums:
            s += num
            x = num + (x if x > 0 else 0)
            y = num + (y if y < 0 else 0)
            max_s = max(x, max_s)
            min_s = min(y, min_s)
        
        return max_s if max_s < 0 else max(max_s, s - min_s)

        

        

