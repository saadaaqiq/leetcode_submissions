# https://leetcode.com/problems/maximum-length-of-pair-chain

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort()
        dp = [1] * n
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if pairs[j][0] > pairs[i][1]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)