# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, pre: List[int], ino: List[int]) -> Optional[TreeNode]:
            if not pre:  return None
            if len(pre)==1:  return TreeNode(pre[0])
            ino_ind = ino.index(pre[0])
            return TreeNode(pre[0], self.buildTree(pre[1:1+ino_ind], ino[:ino_ind]), self.buildTree(pre[1+ino_ind:], ino[ino_ind+1:]))

        


