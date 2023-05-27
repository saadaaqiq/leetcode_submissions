# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree

class Solution:
  def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
    res = 0
    dic = { k:0 for k in range(1,10) }
    
    def existsPal():
      c = 0
      for k in dic:
        if dic[k] % 2 == 1:
          c += 1
      return c == 0 or c == 1
    
    def dfs(node):
      nonlocal res
      dic[node.val] += 1
      if not node.right and not node.left and existsPal():
        res += 1
      if node.right:  
        dfs(node.right)
      if node.left:
        dfs(node.left)
      dic[node.val] -= 1

    dfs(root)
    
    return res