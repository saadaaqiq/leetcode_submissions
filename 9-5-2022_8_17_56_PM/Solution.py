# https://leetcode.com/problems/closest-binary-search-tree-value

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def closestValue(self, root: Optional[TreeNode], target: float) -> int:
    mini, v = abs(root.val - target), root.val
    stack = [root]
    while stack:
      node = stack.pop()
      if abs(node.val-target) < mini:
        mini, v = abs(node.val-target), node.val
      if node.left:
        stack.append(node.left)
      if node.right:
        stack.append(node.right)
    return v