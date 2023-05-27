# https://leetcode.com/problems/largest-rectangle-in-histogram

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        res = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                res = max(res, heights[stack.pop()] * (i-stack[-1]-1))
            stack.append(i)
        heights.pop()
        return res


