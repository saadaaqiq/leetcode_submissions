# https://leetcode.com/problems/convert-bst-to-greater-tree

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node, acc):
            if not node:
                return 0
            r = dfs(node.right, acc)
            l = dfs(node.left, acc + r + node.val)
            s = node.val + r + l
            node.val += acc + r
            return s

        dfs(root, 0)
        return root
            

