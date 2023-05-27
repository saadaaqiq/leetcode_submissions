# https://leetcode.com/problems/path-sum-ii

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        if not root: 
            return res
        
        def dfs(node, path, pathsum):
            if not node.left and not node.right and node.val + pathsum == targetSum:
                res.append(path + [node.val])
            if node.left:
                dfs(node.left, path + [node.val], pathsum + node.val)
            if node.right:
                dfs(node.right, path + [node.val], pathsum + node.val)
        
        dfs(root, [], 0)
        
        return res