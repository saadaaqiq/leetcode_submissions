# https://leetcode.com/problems/find-duplicate-subtrees

class Solution:
    def findDuplicateSubtrees(self, root):

        @cache
        def compare_nodes(node1, node2):
            if not node1 and not node2:
                return True
            if (node1 and not node2) or (not node1 and node2) or (node1.val != node2.val):
                return False
            return compare_nodes(node1.left, node2.left) and compare_nodes(node1.right, node2.right)

        res = []

        dic = collections.defaultdict(list)

        def dfs(node):
            if not node:
                return 
            dic[node.val].append(node)
            dfs(node.left)
            dfs(node.right)
            return
        
        dfs(root)
        vis = set()
        for k in dic:
            n = len(dic[k])
            for i in range(n-1):
                if dic[k][i] in vis:
                    continue
                b = False
                for j in range(i+1, n):
                    if compare_nodes(dic[k][i], dic[k][j]):
                        b = True
                        vis.add(dic[k][i])
                        vis.add(dic[k][j])
                if b:
                    res.append(dic[k][i])                

        return res
            