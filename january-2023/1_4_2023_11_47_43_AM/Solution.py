# https://leetcode.com/problems/target-sum

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def ways(l, t):
            return ways(l+1,t+nums[l]) + ways(l+1,t-nums[l]) if l < len(nums)-1 else (1 if t+nums[l]==target else 0) + (1 if t-nums[l]==target else 0)
        
        return ways(0, 0)