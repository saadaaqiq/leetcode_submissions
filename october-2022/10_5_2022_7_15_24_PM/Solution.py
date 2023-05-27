# https://leetcode.com/problems/add-one-row-to-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def addOneRow(self, root, val, depth):
    if depth == 1:
      return TreeNode(val, root, None)
    q = deque([(root, 2)])
    while q:
      node, d = q.popleft()
      if d == depth:
        node.left = TreeNode(val, node.left, None)
        node.right = TreeNode(val, None, node.right)
      else:
        if node.left: q.append((node.left, d+1))
        if node.right: q.append((node.right, d+1))
    return root
      