# https://leetcode.com/problems/all-possible-full-binary-trees

class Solution:
    @lru_cache
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n%2 == 0: return [] 
        if n==1: return [TreeNode(0)]
        res = []
        for i in range(1, n):
            if i%2 != 0:
                for left in self.allPossibleFBT(i):
                    for right in self.allPossibleFBT(n-1-i):
                        res.append(TreeNode(0, left, right))
        return res
        
