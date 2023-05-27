# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def bstFromPreorder(self, preorder):
    stack = []
    root = None
    for num in preorder:
      node = TreeNode(num)
      if not root: root = node
      last = None
      while stack and stack[-1].val < num: last = stack.pop()
      if last: last.right = node
      elif stack: stack[-1].left = node
      stack.append(node)
    return root