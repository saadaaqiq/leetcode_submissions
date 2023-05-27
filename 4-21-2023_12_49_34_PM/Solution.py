# https://leetcode.com/problems/profitable-schemes

class Solution:
    def profitableSchemes(self, n, mp, G, P):
        MOD = 10**9 + 7
        matrix = [[[0]*(mp+1) for _ in range(n+1)] for _ in range(len(G)+1)]
        for k in range(n+1):
            matrix[len(G)][k][mp] = 1
        for i in range(len(G)-1, -1, -1):
            for k in range(n+1):
                for p in range(mp+1):
                    matrix[i][k][p] = matrix[i+1][k][p] % MOD
                    if k + G[i] <= n: 
                        matrix[i][k][p] += matrix[i+1][k+G[i]][min(mp,p+P[i])] % MOD
        return matrix[0][0][0] % MOD
                    
