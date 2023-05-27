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
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def dfs(arr):
            if not arr:
                return [ None ]
            res = []
            for i in range(len(arr)):
                for l in dfs(arr[:i]):
                    for r in dfs(arr[i+1:]):
                        root = TreeNode(arr[i])
                        root.left = l
                        root.right = r
                        res.append(root)
            return res
        
        return dfs([i for i in range(1, n+1)])



        
        













            

                    