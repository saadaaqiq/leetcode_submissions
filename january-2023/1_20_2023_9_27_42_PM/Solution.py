# https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        curr = []

        def backtrack(i):
            if i == len(nums):
                res.append(curr.copy())
                return
            # include nums[i]
            curr.append(nums[i])
            backtrack(i+1)
            curr.pop()
            # don't include nums[i]
            backtrack(i+1)
            return
        
        backtrack(0)
        
        return res