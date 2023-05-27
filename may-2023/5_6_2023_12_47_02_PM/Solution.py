# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n, MOD, res, r = len(nums), 10**9 + 7, 0, len(nums)-1
        nums.sort()
        for l in range(n):
            while r >= l and nums[l] + nums[r] > target:
                r -= 1
            # r is fixed now, so the possible results including this r
            # are subsets of nums[l:r], of length (r-l)
            # the number of subsets is given with the formula
            # 2 ** (length of subset), aka 2**(r-l)
            if r >= l:
                res += 2**(r-l) % MOD
        return res % MOD