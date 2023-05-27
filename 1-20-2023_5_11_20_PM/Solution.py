# https://leetcode.com/problems/non-decreasing-subsequences

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        curr = []

        def backtrack(i):
            if i==len(nums):
                if len(curr)>1:
                    res.add(tuple(curr))
                return 
            if not curr or nums[i] >= curr[-1]:
                curr.append(nums[i])
                backtrack(i+1)
                curr.pop()
            backtrack(i+1)
            return 
            
        backtrack(0)
        return res