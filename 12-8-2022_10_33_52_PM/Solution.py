# https://leetcode.com/problems/leaf-similar-trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        stack = []
        def dfs(node):
            if node.left: dfs(node.left)
            if node.right: dfs(node.right)
            if not node.left and not node.right: stack.append(node.val)
        dfs(root1)
        def check(node):
            if node.right: 
                if not check(node.right): 
                    return False
            if node.left:
                if not check(node.left): 
                    return False
            if not node.left and not node.right:
                if not stack or stack.pop() != node.val:
                    return False
            return True
        return check(root2) and not stack