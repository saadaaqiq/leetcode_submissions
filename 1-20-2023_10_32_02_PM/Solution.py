# https://leetcode.com/problems/subsets-ii

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        curr = []

        def backtrack(i):
            if i == len(nums):
                res.append(curr.copy())
                return
            # yes
            curr.append(nums[i])
            backtrack(i+1)
            curr.pop()
            # nope
            j = i
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            backtrack(j)
            return
        
        backtrack(0)
        return res
            