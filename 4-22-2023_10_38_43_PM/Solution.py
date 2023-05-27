# https://leetcode.com/problems/convert-bst-to-greater-tree

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
            
        def dfs(node, s):
            l, r = 0, 0
            if node.right:
                r = dfs(node.right, s)
            if node.left:
                l = dfs(node.left, s + r + node.val)
            node.val = node.val + s + r
            return node.val - s + l
        
        dfs(root, 0)
        return root