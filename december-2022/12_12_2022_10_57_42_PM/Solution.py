# https://leetcode.com/problems/binary-tree-maximum-path-sum

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = -float("infinity")

        def dfs(node):
            nonlocal res
            l = max(dfs(node.left),0) if node.left else 0
            r = max(dfs(node.right),0) if node.right else 0
            res = max(res, node.val + l + r)
            return node.val + max(l,r)

        dfs(root)
        return res
        