# https://leetcode.com/problems/burst-balloons

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        @cache        
        def dfs(l, r):
            if l > r:
                return 0
            return max([nums[l-1]*nums[i]*nums[r+1] + dfs(l, i-1) + dfs(i+1, r) for i in range(l, r+1)])

        return dfs(1, len(nums)-2)