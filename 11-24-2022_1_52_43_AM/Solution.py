# https://leetcode.com/problems/largest-rectangle-in-histogram

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        a = [-heights[i] for i in range(n)]
        s = []
        m = 0
        for i in range(-1,n+1):
            h = heights[i] if 0<=i<n else 0
            while s and h < s[-1][1]:
                k, hk = s.pop()
                a[k] += (i-k)*hk
            s.append((i,h))
        s.clear()
        for i in range(n,-2,-1):
            h = heights[i] if 0<=i<n else 0
            while s and h < s[-1][1]:
                k,hk = s.pop()
                a[k] += (k-i)*hk
                m = max(m,a[k])
            s.append((i,h))
        return m