# https://leetcode.com/problems/flatten-binary-tree-to-linked-list

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        
        def dfs(node):
            if not node.left and not node.right:
                return node, node
            li, lf, ri, rf = None, None, None, None
            if node.left:
                li, lf = dfs(node.left)
            if node.right:
                ri, rf = dfs(node.right)
            node.left = None
            path_end = None
            if li:
                node.right = li
                path_end = lf
                if ri:
                    lf.right = ri
                    path_end = rf
            elif ri:
                node.right = ri
                path_end = rf
            return node, path_end

        dfs(root)