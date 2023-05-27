# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, pre: List[int], ino: List[int]) -> Optional[TreeNode]:
        if not pre:  
            return None
        i = ino.index(pre[0])
        return TreeNode(pre[0], self.buildTree(pre[1:1+i], ino[:i]), self.buildTree(pre[1+i:], ino[i+1:]))

        


