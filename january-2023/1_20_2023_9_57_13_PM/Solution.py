# https://leetcode.com/problems/subsets-ii

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        A = set()
        curr = []

        nums.sort()
        
        def backtrack(i):
            if i == len(nums):
                A.add(tuple(curr))
                return 
            # include i
            curr.append(nums[i])
            backtrack(i+1)
            curr.pop()
            # don't include i
            backtrack(i+1)
            return 

        backtrack(0)

        return A