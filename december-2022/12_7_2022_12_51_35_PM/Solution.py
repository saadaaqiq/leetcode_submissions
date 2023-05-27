# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def dfs(pre, ino):
            if not pre: 
                return None
            if len(pre)==1: 
                return TreeNode(pre[0])
            rootval = pre[0]
            ino_ind = ino.index(rootval)

            left_ino = ino[:ino_ind]
            right_ino = ino[ino_ind+1:]

            left_pre = pre[1:1+ino_ind]
            right_pre = pre[1+ino_ind:]

            return TreeNode(rootval, dfs(left_pre, left_ino), dfs(right_pre, right_ino))

        return dfs(preorder, inorder)
        


