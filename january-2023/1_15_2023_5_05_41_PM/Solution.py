# https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, heights: List[int]) -> int:
        n = len(heights)
        left = [0] * n
        l = 0
        for i in range(n):
            h = heights[i]
            if h >= l:
                l = h
            else: 
                left[i] = l - h
        right = [0] * n
        r = 0
        for i in range(n-1, -1, -1):
            h = heights[i]
            if h >= r:
                r = h
            else:
                right[i] = r - h
        arr = [min(left[i], right[i]) for i in range(n)]
        return sum(arr)
