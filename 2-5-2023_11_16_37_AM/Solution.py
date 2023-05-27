# https://leetcode.com/problems/zigzag-conversion

class Solution:
    def convert(self, s: str, m: int) -> str:
        grid = [[] for i in range(m)]
        i = j = 0
        rev = False
        while j < len(s):
            grid[i].append(s[j])
            j += 1
            if m == 1: continue
            if i == 0:
                rev = False
            if i == m-1:
                rev = True
            if not rev and i < m-1:
                i += 1
            if rev and i > 0:
                i -= 1
        return ''.join([''.join(c for c in r) for r in grid])