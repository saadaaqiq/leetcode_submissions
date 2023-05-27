# https://leetcode.com/problems/binary-tree-maximum-path-sum

class Solution:
  
  def maxPathSum(self, root: Optional[TreeNode]) -> int:
    res = [root.val]
    
    def dfs(node):
      l = dfs(node.left) if node.left else 0
      l = max(l, 0)
      r = dfs(node.right) if node.right else 0
      r = max(r, 0)
      res.append(l+r+node.val)
      return node.val + max(l,r)
    
    s = dfs(root)
    return max(res)