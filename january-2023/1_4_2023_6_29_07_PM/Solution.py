# https://leetcode.com/problems/recover-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        A = []
        last = None
        def dfs(node):
            nonlocal last
            if node.left:
                dfs(node.left)            
            if last and node.val < last.val:
                A.append(last)
                A.append(node)
            last = node
            if node.right:
                dfs(node.right)
        dfs(root)
        A[0].val, A[-1].val = A[-1].val, A[0].val
            


        
        
        


            
            
        
        






        
        