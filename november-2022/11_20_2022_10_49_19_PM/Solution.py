# https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        nset = set(nums)
        def dfs(arr):
            if len(arr) == len(nums):
                res.append(arr)
            for k in nset - set(arr):
                dfs(arr + [k])
        dfs([])
        return res