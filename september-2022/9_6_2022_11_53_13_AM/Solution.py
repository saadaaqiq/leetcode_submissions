# https://leetcode.com/problems/binary-tree-pruning

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def pruneTree(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
    if not node: return None
    node.right, node.left = self.pruneTree(node.right), self.pruneTree(node.left)
    return node if (node.val == 1 or node.right or node.left) else None

      
    