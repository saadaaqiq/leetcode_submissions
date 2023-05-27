# https://leetcode.com/problems/combination-sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        stack = []
        cur_sum = 0
        res = []

        def backtrack(i):
            nonlocal cur_sum
            if cur_sum > target:
                return 
            if cur_sum == target:
                res.append(stack.copy())
                return 
            if i >= n:
                return 
            # including the current candidate and trying again
            cur_sum += candidates[i]
            stack.append(candidates[i])
            backtrack(i)
            stack.pop()
            cur_sum -= candidates[i]
            # not including him
            backtrack(i+1)
            return 

        backtrack(0)
        return res