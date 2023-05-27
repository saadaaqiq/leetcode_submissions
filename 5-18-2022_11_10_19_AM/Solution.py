# https://leetcode.com/problems/kth-smallest-element-in-a-bst

class Solution:
  def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    
    tab = []
    
    def dfs(node):
      if node:
        dfs(node.left)
        tab.append(node.val)
        dfs(node.right)
        
    dfs(root)
    
    return tab[k-1]