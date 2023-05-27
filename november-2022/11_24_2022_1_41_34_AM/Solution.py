# https://leetcode.com/problems/largest-rectangle-in-histogram

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        heights.insert(0,0)
        n = len(heights)
        a1, a2 = [0]*n, [0]*n
        s1, s2 = [], []
        for i in range(n):
            h = heights[i]
            while s1 and h<s1[-1][1]:
                i1,h1 = s1.pop()
                a1[i1] = (i-i1)*h1
            s1.append((i,h))
        for i in range(n-1,-1,-1):
            h = heights[i]
            while s2 and h<s2[-1][1]:
                i2,h2 = s2.pop()
                a2[i2] = (i2-i)*h2
            s2.append((i,h))
        print(a1)
        print(a2)
        return max([a1[i]+a2[i]-heights[i] for i in range(n)])