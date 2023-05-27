# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        n = len(mat[0])
        for i, row in enumerate(mat):
            l, r = 0, n
            while l < r:
                mid = (l+r)//2
                if row[mid]==1:
                    l = mid + 1
                else:
                    r = mid
            res.append((l,i))
        res.sort()

        return list(zip(*res))[1][:k]