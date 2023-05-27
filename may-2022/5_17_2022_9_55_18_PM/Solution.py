# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

    def reconstruct(preorder, inorder):
      if not preorder:
        return None
      if len(preorder) == 1:
        return TreeNode(preorder[0])
      p = 0
      first = inorder[:inorder.index(preorder[p])]
      second = inorder[inorder.index(preorder[p])+1:]
      node = TreeNode()
      node.val = preorder[p]
      p+=1
      node.left = reconstruct(preorder[p:p+len(first)], first)
      node.right = reconstruct(preorder[p+len(first):p+len(first)+len(second)], second)
      return node
      
    return reconstruct(preorder, inorder)
    