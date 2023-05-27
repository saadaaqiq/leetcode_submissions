# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree

class Solution:
  def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
    res = 0
    odds = set()
    
    def dfs(node):
      nonlocal res
      if node.val in odds: odds.remove(node.val)
      else: odds.add(node.val)
      if not node.right and not node.left and len(odds) <= 1:
        res += 1
      if node.right:  
        dfs(node.right)
      if node.left:
        dfs(node.left)
      if node.val in odds: odds.remove(node.val)
      else: odds.add(node.val)

    dfs(root)
    
    return res