# https://leetcode.com/problems/unique-binary-search-trees

class Solution:
    def numTrees(self, n: int) -> int:
        cache = {0: 1, 1: 1}
        for k in range(2, n+1):
            cache[k] = sum([cache[i] * cache[k-i-1] for i in range(k)])
        return cache[n]
                

        