# https://leetcode.com/problems/binary-tree-paths

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
    res = []
    
    def dfs(node, path):
      newpath = path + "->" + str(node.val) if path else str(node.val)
      if not node.left and not node.right:
        res.append(newpath)
      if node.left:
        dfs(node.left, newpath)
      if node.right:
        dfs(node.right, newpath)
      
    dfs(root, "")
    return res