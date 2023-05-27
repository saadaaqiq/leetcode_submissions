# https://leetcode.com/problems/path-sum-iii

class Solution:
  def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    
    res = 0
    if not root:
      return res

    def explore(node, s):
      nonlocal res
      if s + node.val == targetSum:
        res += 1
      if node.left:
        explore(node.left, s + node.val)
      if node.right:
        explore(node.right, s + node.val)

    def dfs(node):
      explore(node, 0)
      if node.left:
        dfs(node.left)
      if node.right:
        dfs(node.right)
    
    dfs(root)
    return res