# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def lowestCommonAncestor(self, root, p, q):
    p_anc, q_anc = [root], [root]

    def dfs(node, target, ancestors):
      if node == target: return True
      if node.left:
        ancestors.append(node.left)
        if not dfs(node.left, target, ancestors):
          ancestors.pop()
        else:
          return True
      if node.right:
        ancestors.append(node.right)
        if not dfs(node.right, target, ancestors):
          ancestors.pop()
          return False
        else:
          return True
      return False
    
    dfs(root, p, p_anc)
    dfs(root, q, q_anc)

    i, j = 0, 0
    while i < len(p_anc) and j < len(q_anc) and p_anc[i] == q_anc[j]:
      i += 1
      j += 1
    return p_anc[i-1]
      





          