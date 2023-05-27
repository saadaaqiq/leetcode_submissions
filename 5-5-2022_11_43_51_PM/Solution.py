# https://leetcode.com/problems/binary-tree-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        visited = set()
        
        def dfs(node):
            if not node:
                return
            if node.left and node.left not in visited:
                dfs(node.left)
            res.append(node.val)
            visited.add(node)
            if node.right and node.right not in visited:
                dfs(node.right)
                
        dfs(root)
        return res