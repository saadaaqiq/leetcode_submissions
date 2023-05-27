# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return 0
            node.val = node.val + dfs(node.left) + dfs(node.right)
            return node.val

        prev = dfs(root)
        res = 0

        def rec(node):
            nonlocal res, prev
            v = node.val
            l = node.left.val if node.left else 0
            r = node.right.val if node.right else 0
            res = max(res, (prev-r)*r, (prev-l)*l)
            if node.left:
                rec(node.left)
            if node.right:
                rec(node.right)

        rec(root)
        return res % (10**9 + 7) 









