# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node, p, q):
            nonlocal res
            p = min(p, node.val)
            q = max(q, node.val)
            res = max(res, abs(node.val - p), abs(node.val - q))
            if node.left:
                dfs(node.left, p, q)
            if node.right:
                dfs(node.right, p, q)
        
        dfs(root, float("infinity"), -float("infinity"))
        return res