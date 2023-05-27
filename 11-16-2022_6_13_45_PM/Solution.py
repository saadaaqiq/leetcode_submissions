# https://leetcode.com/problems/unique-binary-search-trees-ii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class MultiNode:
    def __init__(self, val=0):

        self.val = val
        self.left = []
        self.right = []

class Solution:
    def generateTrees(self, n: int):

        def dfs(start, end):
            if start == end:
                return [ None ]
            res = []
            for i in range(start, end):
                for l in dfs(start, i):
                    for r in dfs(i+1, end):
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        res.append(root)
            return res
        
        return dfs(1,n+1)



        
        













            

                    