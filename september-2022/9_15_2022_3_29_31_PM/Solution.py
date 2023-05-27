# https://leetcode.com/problems/find-leaves-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  
  def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
    
    step, res = [], []
    
    def dfs(parent, isLeft, node):
      if not node.right and not node.left:
        step.append(node.val)
        if parent and isLeft: parent.left = None
        if parent and not isLeft: parent.right = None
        if not parent: return False
      else:
        if node.left:
          dfs(node, True, node.left)
        if node.right:
          dfs(node, False, node.right)
      return True
    
    while root:
      b = dfs(None, False, root)
      res.append(step)
      if b:
        step = []
      else:
        break
    
    return res
    
        
        
        
        
        
        
        
        
      
      
        
      