# https://leetcode.com/problems/profitable-schemes

class Solution:
    def profitableSchemes(self, n, minProfit, group, profit):
        MOD = 10**9 + 7

        def bottom_up():
            dp = collections.defaultdict(int)
            for k in range(n+1):
                dp[(len(group), k, minProfit)] = 1
            for i in range(len(group)-1, -1, -1):
                for k in range(n+1):
                    for p in range(minProfit+1):
                        dp[(i, k, p)] = dp[(i+1, k, p)]
                        if k + group[i] <= n:
                            dp[(i, k, p)] += dp[(i+1, k+group[i], min(minProfit, p+profit[i]))] % MOD
            return dp[(0,0,0)] % MOD

        @cache
        def top_down(i, k, p):
            if i >= len(group):
                return 1 if p >= minProfit else 0
            return (top_down(i+1, k+group[i], p+profit[i]) % MOD if k+group[i]<=n else 0) + (top_down(i+1,k,p) % MOD)
        
        return bottom_up()
