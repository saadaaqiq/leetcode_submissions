# https://leetcode.com/problems/binary-search-tree-iterator

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        def dfs(node):
            if node.right:
                dfs(node.right)
            self.stack.append(node)
            if node.left:
                dfs(node.left)
        dfs(root)

    def next(self) -> int:
        return self.stack.pop().val
        
    def hasNext(self) -> bool:
        return len(self.stack) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()