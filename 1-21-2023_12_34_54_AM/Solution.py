# https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = [[]]

        def perm(i):
            arr = []
            for p in res:
                for j in range(len(p)+1):
                    cp = p.copy()
                    cp.insert(j, nums[i])
                    arr.append(cp)
            for x in arr:
                res.append(x)
            return
                
        for i in range(len(nums)):
            perm(i)

        return [t for t in res if len(t) == len(nums)]