# https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values

class Solution:
    def splitString(self, s: str) -> bool:

        n = len(s)

        def dfs(i, v):
            if i >= n:
                return True
            for j in range(i, n):
                w = int(s[i:j+1])
                if w == v - 1 and dfs(j+1, w):
                    return True
            return False

        for i in range(n-1):
            v = int(s[:i+1])
            print(v)
            if dfs(i+1, v):
                return True
        return False

        











