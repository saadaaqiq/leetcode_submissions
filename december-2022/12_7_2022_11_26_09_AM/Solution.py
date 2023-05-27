# https://leetcode.com/problems/range-sum-of-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def dfs(node):
            res = 0
            if node.val < low:
                if node.right:
                    res += dfs(node.right)
            elif node.val > high:
                if node.left:
                    res += dfs(node.left)
            else:
                res += node.val
                if node.right: res += dfs(node.right)
                if node.left: res += dfs(node.left)
            return res


        
        return dfs(root)