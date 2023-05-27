# https://leetcode.com/problems/sum-of-all-subset-xor-totals

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        cur = 0
        def backtrack(i):
            nonlocal cur, res
            if i == n:
                res += cur
                return
            if cur==0:
                cur = nums[i]
                backtrack(i+1)
                cur = 0
            else:
                cur ^= nums[i]
                backtrack(i+1)
                cur ^= nums[i]
            backtrack(i+1)
        backtrack(0)
        return res