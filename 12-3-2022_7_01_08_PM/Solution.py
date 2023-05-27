# https://leetcode.com/problems/all-possible-full-binary-trees

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        

        @lru_cache
        def dfs(k):
            if k%2 == 0: return [] 
            if k==1: return [TreeNode(0)]
            res = []
            for i in range(1, k):
                if i%2 != 0:
                    for left in dfs(i):
                        for right in dfs(k-1-i):
                            res.append(TreeNode(0, left, right))
            return res
        
        return dfs(n)

