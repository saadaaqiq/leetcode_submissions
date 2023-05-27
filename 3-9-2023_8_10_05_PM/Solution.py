# https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prv = nums[0]
        A = [1]
        for i in range(1, n):
          A.append(prv)
          prv *= nums[i]
        nxt = nums[n-1]
        B = [1]
        for i in range(n-2, -1, -1):
          B.append(nxt)
          nxt *= nums[i]
        B.reverse()
        return [A[i] * B[i] for i in range(n)]