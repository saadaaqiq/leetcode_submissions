# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def longestConsecutive(self, root: Optional[TreeNode]) -> int:
    m = 0
    def dfs(node, parent, pathLen):
      nonlocal m
      c = pathLen
      if not parent or node.val != parent.val + 1:
        c = 1
      else:
        c += 1
      m = max(m, c)
      if node.left:
        dfs(node.left, node, c)
      if node.right:
        dfs(node.right, node, c)
    dfs(root, None, 0)
    return m
    