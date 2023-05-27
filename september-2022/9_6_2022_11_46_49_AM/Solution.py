# https://leetcode.com/problems/binary-tree-pruning

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def pruneTree(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
      if not node:
        return None
      if node.val == 1:
        node.right = node.right if self.pruneTree(node.right) else None
        node.left = node.left if self.pruneTree(node.left) else None
        return node
      if node.val == 0:
        node.right = node.right if self.pruneTree(node.right) else None
        node.left = node.left if self.pruneTree(node.left) else None
        return None if (not node.right and not node.left) else node
      
    