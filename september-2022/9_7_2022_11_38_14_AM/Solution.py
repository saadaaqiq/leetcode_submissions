# https://leetcode.com/problems/construct-string-from-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def tree2str(self, node: Optional[TreeNode]) -> str:
    return str(node.val) + ('('+self.tree2str(node.left)+')' if node.left else ('()' if node.right else '')) + ('(' + self.tree2str(node.right) + ')' if node.right else '')