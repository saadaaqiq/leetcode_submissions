# https://leetcode.com/problems/count-good-nodes-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def goodNodes(self, root: TreeNode) -> int:
    good = 0
    def dfs(node, maxi):
      nonlocal good
      if node.val >= maxi:
        good += 1
      if node.right:
        dfs(node.right, max(maxi, node.val))
      if node.left:
        dfs(node.left, max(maxi, node.val))
    dfs(root, -10001)
    return good