# https://leetcode.com/problems/maximum-depth-of-n-ary-tree

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        res = 0
        def dfs(node, l):
            nonlocal res
            if not node.children:
                res = max(res, l)
            for child in node.children:
                dfs(child, l+1)
        dfs(root, 1)
        return res
