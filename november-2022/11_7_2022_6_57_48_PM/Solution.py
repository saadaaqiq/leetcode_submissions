# https://leetcode.com/problems/n-ary-tree-preorder-traversal

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            for i in range(len(node.children)-1, -1, -1):
                stack.append(node.children[i])
        return res