# https://leetcode.com/problems/binary-tree-maximum-path-sum

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = -float("infinity")

        def dfs(node):
            nonlocal res
            v = node.val
            l, nl, r, nr, nrl = -float("infinity"),-float("infinity"),-float("infinity"),-float("infinity"),-float("infinity")
            if node.left:
                l = dfs(node.left)
                nl = v + l
            if node.right:
                r = dfs(node.right)
                nr = v + r
            if node.left and node.right:
                nrl = v + r + l
            if l > nl:
                res = max(res, nl)
            if r > nr:
                res = max(res, nr)
            if nrl > nr and nrl > nl and nrl > v:
                res = max(res, nrl)
            maxi = max(v, nr, nl)
            res = max(maxi, res)
            return maxi

        dfs(root)

        return res
        