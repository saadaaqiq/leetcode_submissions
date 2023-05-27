# https://leetcode.com/problems/binary-tree-maximum-path-sum

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = -float("infinity")

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            l, r = dfs(node.left), dfs(node.right)
            res = max(res, node.val, node.val + l, node.val + r, node.val + l + r)
            return node.val + max(0,l,r)
        
        dfs(root)

        return res
