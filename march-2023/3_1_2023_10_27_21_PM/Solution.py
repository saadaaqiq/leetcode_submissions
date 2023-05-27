# https://leetcode.com/problems/construct-quad-tree

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        def function(grid, i0, i1, j0, j1):
            z, o = False, False
            for k in range(i0, i1+1):
                for l in range(j0, j1+1):
                    if grid[k][l] == 0:
                        z = True
                    else:
                        o = True
                    if z and o:
                        break
                if z and o:
                    break
            if z and o:
                top_left = function(grid, i0, (i0+i1)//2, j0, (j0+j1)//2)
                top_right = function(grid, i0, (i0+i1)//2, (j0+j1)//2 + 1, j1)
                bottom_left = function(grid, (i0+i1)//2 + 1, i1, j0, (j0+j1)//2)
                bottom_right = function(grid, (i0+i1)//2 + 1, i1, (j0+j1)//2 + 1, j1)
                return Node(0, False, top_left, top_right, bottom_left, bottom_right)
            elif z:
                return Node(0, True, None, None, None, None)
            elif o:
                return Node(1, True, None, None, None, None)
            else:
                return None

        return function(grid, 0, n-1, 0, n-1)