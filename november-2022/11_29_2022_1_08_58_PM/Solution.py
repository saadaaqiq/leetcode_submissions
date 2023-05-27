# https://leetcode.com/problems/evaluate-boolean-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def evaluateTree(self, root: Optional[TreeNode]) -> bool:
    if not root.right and not root.left:
      return True if root.val == 1 else False
    return self.evaluateTree(root.right) and self.evaluateTree(root.left) if root.val == 3 else self.evaluateTree(root.right) or self.evaluateTree(root.left)

