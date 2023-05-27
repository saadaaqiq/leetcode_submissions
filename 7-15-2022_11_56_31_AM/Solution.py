# https://leetcode.com/problems/minimum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def minDepth(self, root: Optional[TreeNode]) -> int:
    
    def path(node):
      if not node:
        return 0
      if node.right and node.left:
        return min(path(node.right) + 1, path(node.left) + 1)
      if node.right and not node.left:
        return path(node.right) + 1
      if node.left and not node.right:
        return path(node.left) + 1
      return 1
    
    return path(root)