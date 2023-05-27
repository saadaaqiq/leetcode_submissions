# https://leetcode.com/problems/132-pattern

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        stack = []
        for x in nums:
            xl = x
            while stack and stack[-1][0] < x:
                y, yl = stack.pop()
                xl = min(xl, yl)
            if stack and x < stack[-1][0] and stack[-1][1] < x:
                return True                
            stack.append([x, xl])
        return False