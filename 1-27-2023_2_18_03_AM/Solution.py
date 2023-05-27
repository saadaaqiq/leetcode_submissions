# https://leetcode.com/problems/maximum-subarray-min-product

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        
        res = 0
        stack = []
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        for i, x in enumerate(nums):
            new_start = i
            while stack and x < stack[-1][1]:
                j, y = stack.pop()
                total = prefix[i] - prefix[j]
                res = max(res, total * y)
                new_start = j
            stack.append((new_start, x))
        for i, x in stack:
            total = prefix[len(nums)] - prefix[i]
            res = max(res, total * x)
        return res % (10**9 + 7)


