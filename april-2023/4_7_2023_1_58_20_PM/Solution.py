# https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])
        mat = [[(1 if pizza[i][j]=="A" else 0) for j in range(n)] for i in range(m)]
        mat.append([0]*n)
        for row in mat:
            row.append(0)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                mat[i][j] += mat[i][j+1] - mat[i+1][j+1] + mat[i+1][j]

        for i in range(m+1):
            for j in range(n+1):
                print(mat[i][j], end="\t")
            print()
        
        @cache
        def dfs(i, j, cut, ignore, cache):
            if cut == 1:
                return 1 if mat[i][j] > 0 else 0
            if mat[i][j] == 0:
                return 0
            s = 0
            # making a cut below this row
            if ignore >= 0 and max(mat[i][j], cache) > mat[i+1][j]:
                s += dfs(i+1, j, cut-1, 0, -inf)
            # making a cut right of this column
            if ignore <= 0 and max(mat[i][j], cache) > mat[i][j+1]:
                s += dfs(i, j+1, cut-1, 0, -inf)
            # ignoring this row
            if ignore >= 0:
                s += dfs(i+1, j, cut, 1, max(mat[i][j], cache))
            # ignoring this column
            if ignore <= 0:
                s += dfs(i, j+1, cut, -1, max(mat[i][j], cache))
            return s
            
        
        return dfs(0, 0, k, 0, -inf) % (10**9 + 7)









