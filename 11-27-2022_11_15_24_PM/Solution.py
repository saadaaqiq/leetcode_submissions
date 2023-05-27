# https://leetcode.com/problems/inorder-successor-in-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        found = False

        def dfs(node):
            if not node: return None
            nonlocal found
            if node.left:
                l = dfs(node.left)
                if l: return l
            if found: return node
            elif node == p: found = True
            if node.right: 
                r = dfs(node.right)
                if r: return r
            return None

        return dfs(root)