# https://leetcode.com/problems/find-duplicate-subtrees

class Solution:
    def findDuplicateSubtrees(self, root):

        
        dic = {}

        def serialize(node):
            if not node:
                return "N,"
            s = str(node.val) + "," + serialize(node.left) + serialize(node.right)
            if s not in dic:
                dic[s] = None
            else:
                dic[s] = node
            return s
        
        serialize(root)

        res = []

        for node in dic.values():
            if node:
                res.append(node)

        return res        






        
        