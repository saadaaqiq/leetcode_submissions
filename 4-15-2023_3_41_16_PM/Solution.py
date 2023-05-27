# https://leetcode.com/problems/first-missing-positive

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [0] * n
        for i, j in enumerate(nums):
            if 0 < j <= n:
                arr[j-1] = j
        c = 1
        for i in range(n):
            if c != arr[i]:
                return c
            else:
                c += 1
        return c
        