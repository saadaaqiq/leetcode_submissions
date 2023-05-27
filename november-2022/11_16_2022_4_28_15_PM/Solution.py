# https://leetcode.com/problems/unique-binary-search-trees

class Solution:
    def numTrees(self, n: int) -> int:
        cache = {0: 1, 1: 1}
        
        def rec(k):
            if k not in cache:
                cache[k] = sum([rec(i) * rec(k-i-1) for i in range(k)])
            return cache[k]
        
        return rec(n)
                

        