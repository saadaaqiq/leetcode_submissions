# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary

class Solution:
    def numWays(self, arr: List[str], s: str) -> int:
        l, m, n = len(s), len(arr), len(arr[0])
        counters = []
        for j in range(n):
            counter = collections.Counter()
            for i in range(m):
                counter[arr[i][j]] += 1
            counters.append(counter)

        @cache
        def dfs(j, k):
            if k == l: return 1
            if j == n: return 0
            return counters[j][s[k]] * dfs(j+1, k+1) + dfs(j+1, k)
                
        return dfs(0, 0) % (10**9 + 7)




