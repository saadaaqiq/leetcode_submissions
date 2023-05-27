# https://leetcode.com/problems/recover-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        arr = []
        def dfs(node):
            if node.left:
                dfs(node.left)
            arr.append(node)
            if node.right:
                dfs(node.right)
        dfs(root)
        tab = sorted([node for node in arr], key=lambda node:node.val)
        for i in range(len(arr)):
            if arr[i].val != tab[i].val:
                t = arr[i].val
                arr[i].val = tab[i].val
                tab[i].val = t
                return 



        
        
        


            
            
        
        






        
        