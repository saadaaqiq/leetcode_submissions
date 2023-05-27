# https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, heights: List[int]) -> int:
        n = len(heights)
        left = [heights[0]] + [0] * (n-1)
        right = [0] * (n-1) + [heights[-1]]
        for i in range(1, n):
            left[i] = max(left[i-1], heights[i])
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], heights[i])
        res = 0
        for i in range(n):
            h = min(left[i], right[i])
            res += h-heights[i]
        return res