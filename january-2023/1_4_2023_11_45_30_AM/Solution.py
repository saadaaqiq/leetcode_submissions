# https://leetcode.com/problems/target-sum

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def ways(l, t):
            w = 0
            if l==len(nums)-1:
                if t + nums[l] == target: w+=1
                if t - nums[l] == target: w+=1
            else:
                w1 = ways(l+1,t+nums[l])
                w2 = ways(l+1,t-nums[l])
                w += w1 + w2
            return w
        
        return ways(0, 0)