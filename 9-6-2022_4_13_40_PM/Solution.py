# https://leetcode.com/problems/maximum-average-subtree

class Solution:
  def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
    maxi = 0
    def dfs(node):
      nonlocal maxi
      if not node: return (0,0)
      v_right, cnt_right = dfs(node.right)
      v_left, cnt_left = dfs(node.left)
      t_vals, t_cnt = v_right + v_left + node.val, cnt_right + cnt_left + 1
      maxi = max(maxi, t_vals/t_cnt)
      return (t_vals, t_cnt)
    
    dfs(root)
    
    return maxi