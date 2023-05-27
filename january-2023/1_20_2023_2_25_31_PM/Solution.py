# https://leetcode.com/problems/lonely-pixel-i

class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        lonely, rows, columns = set(), {}, {}
        m, n = len(picture), len(picture[0])
        for i in range(m):
            for j in range(n):
                if picture[i][j] == "B":
                    if i not in rows:
                        rows[i] = 0
                    rows[i] += 1
                    if j not in columns:
                        columns[j] = 0
                    columns[j] += 1
                    lonely.add((i,j))
        res = 0
        for (i,j) in lonely:
            if rows[i] == columns[j] == 1:
                res += 1
        return res