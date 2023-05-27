# https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def perm(i):
            if i == len(nums):
                return [[]]
            res = []
            P = perm(i+1)
            for p in P:
                for j in range(len(p)+1):
                    p_copy = p.copy()
                    p_copy.insert(j, nums[i])
                    res.append(p_copy)
            return res

        return perm(0)