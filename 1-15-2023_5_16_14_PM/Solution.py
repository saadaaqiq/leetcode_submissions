# https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)

        @cache 
        def dfs(i):
            nonlocal n
            if i == n:
                return [[]]
            res = []
            for arr in dfs(i+1):
                res.append(arr)
                res.append([nums[i]] + arr)
            return res

        return dfs(0)