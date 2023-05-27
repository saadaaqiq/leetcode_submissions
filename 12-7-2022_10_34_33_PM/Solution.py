# https://leetcode.com/problems/binary-tree-maximum-path-sum

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = -float("infinity")

        def dfs(node):
            nonlocal res
            v = node.val
            nl, nr, nrl = -float("infinity"),-float("infinity"),-float("infinity")
            if node.left:
                nl = v + dfs(node.left)
            if node.right:
                nr = v + dfs(node.right)
            if node.left and node.right:
                nrl = nl + nr - v
            if nrl > nr and nrl > nl and nrl > v: 
                res = max(res, nrl)
            maxi = max(v, nr, nl)
            res = max(maxi, res)
            return maxi

        dfs(root)

        return res
        