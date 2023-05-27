# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            lx, ly, rx, ry = 0, 0, 0, 0
            if node.left:                
                lx, ly = dfs(node.left)
            if node.right:
                rx, ry = dfs(node.right)
            res = max(res, lx, ry)
            return 1 + ly, 1 + rx
        l, r = dfs(root)
        return max(l, r, res) - 1
            





                
            